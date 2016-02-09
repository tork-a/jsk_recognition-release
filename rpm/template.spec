Name:           ros-jade-jsk-pcl-ros-utils
Version:        0.3.14
Release:        1%{?dist}
Summary:        ROS jsk_pcl_ros_utils package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/jsk_pcl_ros
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       ros-jade-cv-bridge
Requires:       ros-jade-diagnostic-msgs
Requires:       ros-jade-diagnostic-updater
Requires:       ros-jade-dynamic-reconfigure
Requires:       ros-jade-eigen-conversions
Requires:       ros-jade-geometry-msgs
Requires:       ros-jade-image-geometry
Requires:       ros-jade-image-transport
Requires:       ros-jade-image-view2
Requires:       ros-jade-interactive-markers
Requires:       ros-jade-jsk-footstep-msgs
Requires:       ros-jade-jsk-recognition-msgs
Requires:       ros-jade-jsk-recognition-utils
Requires:       ros-jade-jsk-topic-tools
Requires:       ros-jade-kdl-conversions
Requires:       ros-jade-kdl-parser
Requires:       ros-jade-laser-assembler
Requires:       ros-jade-message-runtime
Requires:       ros-jade-moveit-core
Requires:       ros-jade-moveit-ros-perception
Requires:       ros-jade-nav-msgs
Requires:       ros-jade-nodelet
Requires:       ros-jade-octomap
Requires:       ros-jade-octomap-msgs
Requires:       ros-jade-octomap-ros
Requires:       ros-jade-octomap-server
Requires:       ros-jade-pcl-conversions
Requires:       ros-jade-pcl-msgs
Requires:       ros-jade-pcl-ros
Requires:       ros-jade-robot-self-filter
Requires:       ros-jade-rosboost-cfg
Requires:       ros-jade-roscpp-tutorials
Requires:       ros-jade-sensor-msgs
Requires:       ros-jade-std-msgs
Requires:       ros-jade-std-srvs
Requires:       ros-jade-stereo-msgs
Requires:       ros-jade-tf
Requires:       ros-jade-tf-conversions
Requires:       ros-jade-tf2-ros
Requires:       ros-jade-visualization-msgs
Requires:       yaml-cpp-devel
BuildRequires:  boost-devel
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-cv-bridge
BuildRequires:  ros-jade-diagnostic-msgs
BuildRequires:  ros-jade-diagnostic-updater
BuildRequires:  ros-jade-dynamic-reconfigure
BuildRequires:  ros-jade-eigen-conversions
BuildRequires:  ros-jade-geometry-msgs
BuildRequires:  ros-jade-image-geometry
BuildRequires:  ros-jade-image-transport
BuildRequires:  ros-jade-image-view2
BuildRequires:  ros-jade-interactive-markers
BuildRequires:  ros-jade-jsk-footstep-msgs
BuildRequires:  ros-jade-jsk-recognition-msgs
BuildRequires:  ros-jade-jsk-recognition-utils
BuildRequires:  ros-jade-jsk-tools
BuildRequires:  ros-jade-jsk-topic-tools
BuildRequires:  ros-jade-kdl-conversions
BuildRequires:  ros-jade-kdl-parser
BuildRequires:  ros-jade-laser-assembler
BuildRequires:  ros-jade-message-generation
BuildRequires:  ros-jade-moveit-core
BuildRequires:  ros-jade-moveit-ros-perception
BuildRequires:  ros-jade-nav-msgs
BuildRequires:  ros-jade-nodelet
BuildRequires:  ros-jade-octomap
BuildRequires:  ros-jade-octomap-msgs
BuildRequires:  ros-jade-octomap-ros
BuildRequires:  ros-jade-octomap-server
BuildRequires:  ros-jade-pcl-conversions
BuildRequires:  ros-jade-pcl-msgs
BuildRequires:  ros-jade-pcl-ros
BuildRequires:  ros-jade-robot-self-filter
BuildRequires:  ros-jade-rosboost-cfg
BuildRequires:  ros-jade-roscpp-tutorials
BuildRequires:  ros-jade-sensor-msgs
BuildRequires:  ros-jade-std-msgs
BuildRequires:  ros-jade-std-srvs
BuildRequires:  ros-jade-stereo-msgs
BuildRequires:  ros-jade-tf
BuildRequires:  ros-jade-tf-conversions
BuildRequires:  ros-jade-tf2-ros
BuildRequires:  ros-jade-visualization-msgs
BuildRequires:  yaml-cpp-devel

%description
jsk_pcl_ros

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
* Sat Feb 06 2016 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.3.14-1
- Autogenerated by Bloom

* Thu Feb 04 2016 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.3.14-0
- Autogenerated by Bloom

* Wed Feb 03 2016 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.3.13-20
- Autogenerated by Bloom

* Wed Feb 03 2016 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.3.13-19
- Autogenerated by Bloom

* Tue Feb 02 2016 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.3.13-18
- Autogenerated by Bloom

* Mon Feb 01 2016 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.3.13-17
- Autogenerated by Bloom

* Sun Jan 31 2016 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.3.13-16
- Autogenerated by Bloom

* Sat Jan 30 2016 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.3.13-15
- Autogenerated by Bloom

* Fri Jan 29 2016 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.3.13-14
- Autogenerated by Bloom

* Thu Jan 28 2016 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.3.13-13
- Autogenerated by Bloom

* Wed Jan 27 2016 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.3.13-12
- Autogenerated by Bloom

* Tue Jan 26 2016 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.3.13-11
- Autogenerated by Bloom

* Mon Jan 25 2016 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.3.13-10
- Autogenerated by Bloom

* Sun Jan 24 2016 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.3.13-9
- Autogenerated by Bloom

* Sun Jan 24 2016 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.3.13-8
- Autogenerated by Bloom

* Mon Jan 18 2016 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.3.13-7
- Autogenerated by Bloom

* Mon Jan 11 2016 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.3.13-6
- Autogenerated by Bloom

* Mon Jan 04 2016 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.3.13-5
- Autogenerated by Bloom

* Mon Dec 28 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.3.13-4
- Autogenerated by Bloom

* Mon Dec 21 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.3.13-3
- Autogenerated by Bloom

* Sun Dec 20 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.3.13-2
- Autogenerated by Bloom

* Sun Dec 20 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.3.13-1
- Autogenerated by Bloom

