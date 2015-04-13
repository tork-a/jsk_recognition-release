Name:           ros-hydro-jsk-pcl-ros
Version:        0.2.11
Release:        0%{?dist}
Summary:        ROS jsk_pcl_ros package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/jsk_pcl_ros
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       python-scikit-learn
Requires:       ros-hydro-cv-bridge
Requires:       ros-hydro-diagnostic-msgs
Requires:       ros-hydro-diagnostic-updater
Requires:       ros-hydro-dynamic-reconfigure
Requires:       ros-hydro-eigen-conversions
Requires:       ros-hydro-geometry-msgs
Requires:       ros-hydro-image-geometry
Requires:       ros-hydro-image-transport
Requires:       ros-hydro-image-view2
Requires:       ros-hydro-jsk-footstep-msgs
Requires:       ros-hydro-jsk-recognition-msgs
Requires:       ros-hydro-jsk-topic-tools
Requires:       ros-hydro-laser-assembler
Requires:       ros-hydro-message-runtime
Requires:       ros-hydro-ml-classifiers
Requires:       ros-hydro-moveit-core
Requires:       ros-hydro-moveit-ros-perception
Requires:       ros-hydro-nodelet
Requires:       ros-hydro-pcl-conversions
Requires:       ros-hydro-pcl-msgs
Requires:       ros-hydro-pcl-ros
Requires:       ros-hydro-rosboost-cfg
Requires:       ros-hydro-roscpp-tutorials
Requires:       ros-hydro-sensor-msgs
Requires:       ros-hydro-sklearn
Requires:       ros-hydro-std-msgs
Requires:       ros-hydro-std-srvs
Requires:       ros-hydro-stereo-msgs
Requires:       ros-hydro-tf
Requires:       ros-hydro-tf-conversions
Requires:       ros-hydro-tf2-ros
Requires:       ros-hydro-visualization-msgs
Requires:       yaml-cpp-devel
BuildRequires:  boost-devel
BuildRequires:  python-scikit-learn
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-cv-bridge
BuildRequires:  ros-hydro-diagnostic-msgs
BuildRequires:  ros-hydro-diagnostic-updater
BuildRequires:  ros-hydro-dynamic-reconfigure
BuildRequires:  ros-hydro-eigen-conversions
BuildRequires:  ros-hydro-geometry-msgs
BuildRequires:  ros-hydro-image-geometry
BuildRequires:  ros-hydro-image-transport
BuildRequires:  ros-hydro-image-view2
BuildRequires:  ros-hydro-jsk-footstep-msgs
BuildRequires:  ros-hydro-jsk-recognition-msgs
BuildRequires:  ros-hydro-jsk-topic-tools
BuildRequires:  ros-hydro-laser-assembler
BuildRequires:  ros-hydro-message-generation
BuildRequires:  ros-hydro-ml-classifiers
BuildRequires:  ros-hydro-moveit-core
BuildRequires:  ros-hydro-moveit-ros-perception
BuildRequires:  ros-hydro-nodelet
BuildRequires:  ros-hydro-pcl-conversions
BuildRequires:  ros-hydro-pcl-msgs
BuildRequires:  ros-hydro-pcl-ros
BuildRequires:  ros-hydro-rosboost-cfg
BuildRequires:  ros-hydro-roscpp-tutorials
BuildRequires:  ros-hydro-sensor-msgs
BuildRequires:  ros-hydro-sklearn
BuildRequires:  ros-hydro-std-msgs
BuildRequires:  ros-hydro-std-srvs
BuildRequires:  ros-hydro-stereo-msgs
BuildRequires:  ros-hydro-tf
BuildRequires:  ros-hydro-tf-conversions
BuildRequires:  ros-hydro-tf2-ros
BuildRequires:  ros-hydro-visualization-msgs
BuildRequires:  yaml-cpp-devel

%description
jsk_pcl_ros

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Mon Apr 13 2015 Youhei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 0.2.11-0
- Autogenerated by Bloom

* Thu Apr 09 2015 Youhei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 0.2.10-0
- Autogenerated by Bloom

* Wed Apr 01 2015 Youhei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 0.2.9-0
- Autogenerated by Bloom

* Thu Mar 26 2015 Youhei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 0.2.7-0
- Autogenerated by Bloom

* Wed Mar 25 2015 Youhei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 0.2.6-0
- Autogenerated by Bloom

* Tue Mar 17 2015 Youhei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 0.2.5-0
- Autogenerated by Bloom

* Mon Mar 09 2015 Youhei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 0.2.4-0
- Autogenerated by Bloom

* Mon Feb 02 2015 Youhei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 0.2.3-0
- Autogenerated by Bloom

* Fri Jan 30 2015 Youhei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 0.2.2-0
- Autogenerated by Bloom

* Fri Jan 30 2015 Youhei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 0.2.1-0
- Autogenerated by Bloom

* Thu Jan 29 2015 Youhei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 0.2.0-0
- Autogenerated by Bloom

* Sat Jan 24 2015 Youhei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 0.1.33-0
- Autogenerated by Bloom

* Mon Jan 12 2015 Youhei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 0.1.32-0
- Autogenerated by Bloom

* Thu Jan 08 2015 Youhei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 0.1.31-0
- Autogenerated by Bloom

* Wed Dec 24 2014 Youhei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 0.1.30-0
- Autogenerated by Bloom

* Wed Dec 24 2014 Youhei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 0.1.29-0
- Autogenerated by Bloom

* Sun Dec 21 2014 Youhei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 0.1.28-0
- Autogenerated by Bloom

* Tue Dec 09 2014 Youhei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 0.1.27-0
- Autogenerated by Bloom

* Sun Nov 23 2014 Youhei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 0.1.26-0
- Autogenerated by Bloom

* Sat Nov 22 2014 Youhei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 0.1.25-0
- Autogenerated by Bloom

