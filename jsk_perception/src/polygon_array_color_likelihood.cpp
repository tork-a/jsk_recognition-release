// -*- mode: c++ -*-
/*********************************************************************
 * Software License Agreement (BSD License)
 *
 *  Copyright (c) 2015, JSK Lab
 *  All rights reserved.
 *
 *  Redistribution and use in source and binary forms, with or without
 *  modification, are permitted provided that the following conditions
 *  are met:
 *
 *   * Redistributions of source code must retain the above copyright
 *     notice, this list of conditions and the following disclaimer.
 *   * Redistributions in binary form must reproduce the above
 *     copyright notice, this list of conditions and the following
 *     disclaimer in the documentation and/o2r other materials provided
 *     with the distribution.
 *   * Neither the name of the JSK Lab nor the names of its
 *     contributors may be used to endorse or promote products derived
 *     from this software without specific prior written permission.
 *
 *  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
 *  "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
 *  LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
 *  FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
 *  COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
 *  INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
 *  BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
 *  LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
 *  CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
 *  LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
 *  ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
 *  POSSIBILITY OF SUCH DAMAGE.
 *********************************************************************/

#include "jsk_perception/polygon_array_color_likelihood.h"
#include <jsk_recognition_utils/cv_utils.h>

namespace jsk_perception
{
  void PolygonArrayColorLikelihood::onInit()
  {
    DiagnosticNodelet::onInit();
    pnh_->param("approximate_sync", approximate_sync_, false);
    pnh_->param("max_queue_size", max_queue_size_, 10);
    srv_ = boost::make_shared <dynamic_reconfigure::Server<Config> > (*pnh_);
    dynamic_reconfigure::Server<Config>::CallbackType f =
      boost::bind (
        &PolygonArrayColorLikelihood::configCallback, this, _1, _2);
    srv_->setCallback (f);
    pub_ = advertise<jsk_recognition_msgs::PolygonArray>(*pnh_, "output", 1);
  }

  void PolygonArrayColorLikelihood::subscribe()
  {
    sub_reference_ = pnh_->subscribe(
      "input/reference", 1, &PolygonArrayColorLikelihood::referenceCallback, this);
    sub_polygon_.subscribe(*pnh_, "input/polygons", max_queue_size_);
    sub_histogram_.subscribe(*pnh_, "input/histograms", max_queue_size_);
    if (approximate_sync_) {
      async_ = boost::make_shared<message_filters::Synchronizer<ApproximateSyncPolicy> >(100);
      async_->connectInput(sub_polygon_, sub_histogram_);
      async_->registerCallback(
        boost::bind(&PolygonArrayColorLikelihood::likelihood, this, _1, _2));
    }
    else {
      sync_ = boost::make_shared<message_filters::Synchronizer<SyncPolicy> >(100);
      sync_->connectInput(sub_polygon_, sub_histogram_);
      sync_->registerCallback(
        boost::bind(&PolygonArrayColorLikelihood::likelihood, this, _1, _2));
    }
  }

  void PolygonArrayColorLikelihood::unsubscribe()
  {
    sub_reference_.shutdown();
    sub_polygon_.unsubscribe();
    sub_histogram_.unsubscribe();
  }

  void PolygonArrayColorLikelihood::referenceCallback(
    const jsk_recognition_msgs::HistogramWithRange::ConstPtr& ref_msg)
  {
    boost::mutex::scoped_lock lock(mutex_);
    reference_ = ref_msg;
  }

  void PolygonArrayColorLikelihood::configCallback(
    Config &config, uint32_t level)
  {
    boost::mutex::scoped_lock lock(mutex_);
    coefficient_method_ = config.coefficient_method;
  }

  double PolygonArrayColorLikelihood::compareHist(
    const cv::MatND& ref_hist,
    const cv::MatND& target_hist)
  {
    if (coefficient_method_ == 0) {
      return (1.0 + cv::compareHist(ref_hist, target_hist, CV_COMP_CORREL)) / 2.0;
    }
    else if (coefficient_method_ == 1) {
      double x = cv::compareHist(ref_hist, target_hist, CV_COMP_CHISQR);
      return 1/ (x * x + 1);
    }
    else if (coefficient_method_ == 2) {
      return cv::compareHist(ref_hist, target_hist, CV_COMP_INTERSECT);
    }
    else if (coefficient_method_ == 3) {
      return 1.0 - cv::compareHist(ref_hist, target_hist, CV_COMP_BHATTACHARYYA);
    }
    else if (coefficient_method_ == 4 || coefficient_method_ == 5) {
      cv::Mat ref_sig = cv::Mat::zeros(ref_hist.cols, 2, CV_32FC1);
      cv::Mat target_sig = cv::Mat::zeros(ref_hist.cols, 2, CV_32FC1);
      //JSK_NODELET_INFO("ref_hist.cols = %d", ref_hist.cols);
      for (size_t i = 0; i < ref_hist.cols; i++) {
        ref_sig.at<float>(i, 0) = ref_hist.at<float>(0, i);
        target_sig.at<float>(i, 0) = target_hist.at<float>(0, i);
        ref_sig.at<float>(i, 1) = i;
        target_sig.at<float>(i, 1) = i;
      }
      if (coefficient_method_ == 4) {
        double x = cv::EMD(ref_sig, target_sig, CV_DIST_L1);
        return 1.0  / (1.0 + x * x);
      }
      else {
        double x = cv::EMD(ref_sig, target_sig, CV_DIST_L2);
        return 1.0  / (1.0 + x * x);
      }
    }
    else {
      JSK_NODELET_ERROR("unknown coefficiet method: %d", coefficient_method_);
      return 0;
    }
  }
  
  void PolygonArrayColorLikelihood::likelihood(
    const jsk_recognition_msgs::PolygonArray::ConstPtr& polygon_msg,
    const jsk_recognition_msgs::HistogramWithRangeArray::ConstPtr& histogram_msg)
  {
    boost::mutex::scoped_lock lock(mutex_);
    if (!reference_) {
      return;
    }
    if (polygon_msg->polygons.size() != histogram_msg->histograms.size()) {
      JSK_NODELET_ERROR("length of polygon and histogram are not same");
      return;
    }
    cv::MatND reference_histogram
      = jsk_recognition_utils::HistogramWithRangeBinArrayTocvMatND(
        reference_->bins);
    cv::normalize(reference_histogram, reference_histogram, 1, reference_histogram.rows, cv::NORM_L2,
                  -1, cv::Mat());
    jsk_recognition_msgs::PolygonArray new_msg(*polygon_msg);
    for (size_t i = 0; i < new_msg.polygons.size(); i++) {
      cv::MatND hist
        = jsk_recognition_utils::HistogramWithRangeBinArrayTocvMatND(
          histogram_msg->histograms[i].bins);
      cv::normalize(hist, hist, 1, hist.rows, cv::NORM_L2,
                    -1, cv::Mat());
      double d = compareHist(reference_histogram, hist);
      if (polygon_msg->likelihood.size() == 0) {
        new_msg.likelihood.push_back(d);
      }
      else {
        new_msg.likelihood[i] *= d;
      }
    }
    pub_.publish(new_msg);
  }
}

#include <pluginlib/class_list_macros.h>
PLUGINLIB_EXPORT_CLASS (jsk_perception::PolygonArrayColorLikelihood,
                        nodelet::Nodelet);
