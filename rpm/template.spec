Name:           ros-jade-jsk-perception
Version:        0.3.13
Release:        13%{?dist}
Summary:        ROS jsk_perception package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/jsk_perception
Source0:        %{name}-%{version}.tar.gz

Requires:       eigen3-devel
Requires:       ros-jade-angles
Requires:       ros-jade-cv-bridge
Requires:       ros-jade-driver-base
Requires:       ros-jade-dynamic-reconfigure
Requires:       ros-jade-geometry-msgs
Requires:       ros-jade-image-geometry
Requires:       ros-jade-image-transport
Requires:       ros-jade-image-view2
Requires:       ros-jade-jsk-recognition-msgs
Requires:       ros-jade-jsk-recognition-utils
Requires:       ros-jade-jsk-topic-tools
Requires:       ros-jade-message-runtime
Requires:       ros-jade-mk
Requires:       ros-jade-nodelet
Requires:       ros-jade-pcl-ros
Requires:       ros-jade-posedetection-msgs
Requires:       ros-jade-robot-self-filter
Requires:       ros-jade-rosbuild
Requires:       ros-jade-roscpp
Requires:       ros-jade-roseus
Requires:       ros-jade-rospack
Requires:       ros-jade-rospy
Requires:       ros-jade-rostest
Requires:       ros-jade-sensor-msgs
Requires:       ros-jade-std-msgs
Requires:       ros-jade-tf
BuildRequires:  eigen3-devel
BuildRequires:  git
BuildRequires:  ros-jade-angles
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-cmake-modules
BuildRequires:  ros-jade-cv-bridge
BuildRequires:  ros-jade-driver-base
BuildRequires:  ros-jade-dynamic-reconfigure
BuildRequires:  ros-jade-geometry-msgs
BuildRequires:  ros-jade-image-geometry
BuildRequires:  ros-jade-image-transport
BuildRequires:  ros-jade-image-view2
BuildRequires:  ros-jade-jsk-recognition-msgs
BuildRequires:  ros-jade-jsk-recognition-utils
BuildRequires:  ros-jade-jsk-topic-tools
BuildRequires:  ros-jade-message-generation
BuildRequires:  ros-jade-mk
BuildRequires:  ros-jade-nodelet
BuildRequires:  ros-jade-pcl-ros
BuildRequires:  ros-jade-posedetection-msgs
BuildRequires:  ros-jade-robot-self-filter
BuildRequires:  ros-jade-rosbuild
BuildRequires:  ros-jade-roscpp
BuildRequires:  ros-jade-roseus
BuildRequires:  ros-jade-rospack
BuildRequires:  ros-jade-rospy
BuildRequires:  ros-jade-rostest
BuildRequires:  ros-jade-sensor-msgs
BuildRequires:  ros-jade-std-msgs
BuildRequires:  ros-jade-tf

%description
jsk_perception

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Thu Jan 28 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 0.3.13-13
- Autogenerated by Bloom

* Wed Jan 27 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 0.3.13-12
- Autogenerated by Bloom

* Tue Jan 26 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 0.3.13-11
- Autogenerated by Bloom

* Mon Jan 25 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 0.3.13-10
- Autogenerated by Bloom

* Sun Jan 24 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 0.3.13-9
- Autogenerated by Bloom

* Sun Jan 24 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 0.3.13-8
- Autogenerated by Bloom

* Mon Jan 18 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 0.3.13-7
- Autogenerated by Bloom

* Mon Jan 11 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 0.3.13-6
- Autogenerated by Bloom

* Mon Jan 04 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 0.3.13-5
- Autogenerated by Bloom

* Mon Dec 28 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 0.3.13-4
- Autogenerated by Bloom

* Mon Dec 21 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 0.3.13-3
- Autogenerated by Bloom

* Sun Dec 20 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 0.3.13-2
- Autogenerated by Bloom

* Sun Dec 20 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 0.3.13-1
- Autogenerated by Bloom

* Fri Dec 18 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 0.3.11-0
- Autogenerated by Bloom

* Fri Dec 11 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 0.3.8-1
- Autogenerated by Bloom

