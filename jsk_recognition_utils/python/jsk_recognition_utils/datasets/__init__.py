from jsk_recognition_utils.datasets import depth_prediction
from jsk_recognition_utils.datasets import detection
from jsk_recognition_utils.datasets import bbox_detection
from jsk_recognition_utils.datasets import segmentation


DepthPredictionDataset = depth_prediction.DepthPredictionDataset
DetectionDataset = detection.DetectionDataset
BboxDetectionDataset = bbox_detection.BboxDetectionDataset
InstanceSegmentationDataset = segmentation.InstanceSegmentationDataset
SemanticSegmentationDataset = segmentation.SemanticSegmentationDataset
