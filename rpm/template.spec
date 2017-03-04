Name:           ros-kinetic-jsk-pcl-ros-utils
Version:        1.1.1
Release:        0%{?dist}
Summary:        ROS jsk_pcl_ros_utils package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/jsk_pcl_ros
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       python-scikit-learn
Requires:       ros-kinetic-cv-bridge
Requires:       ros-kinetic-diagnostic-msgs
Requires:       ros-kinetic-diagnostic-updater
Requires:       ros-kinetic-dynamic-reconfigure
Requires:       ros-kinetic-eigen-conversions
Requires:       ros-kinetic-geometry-msgs
Requires:       ros-kinetic-image-geometry
Requires:       ros-kinetic-image-transport
Requires:       ros-kinetic-image-view
Requires:       ros-kinetic-image-view2
Requires:       ros-kinetic-interactive-markers
Requires:       ros-kinetic-jsk-data
Requires:       ros-kinetic-jsk-footstep-msgs
Requires:       ros-kinetic-jsk-recognition-msgs
Requires:       ros-kinetic-jsk-recognition-utils
Requires:       ros-kinetic-jsk-topic-tools
Requires:       ros-kinetic-kdl-conversions
Requires:       ros-kinetic-kdl-parser
Requires:       ros-kinetic-laser-assembler
Requires:       ros-kinetic-message-runtime
Requires:       ros-kinetic-moveit-core
Requires:       ros-kinetic-moveit-ros-perception
Requires:       ros-kinetic-nav-msgs
Requires:       ros-kinetic-nodelet
Requires:       ros-kinetic-octomap
Requires:       ros-kinetic-octomap-msgs
Requires:       ros-kinetic-octomap-ros
Requires:       ros-kinetic-octomap-server
Requires:       ros-kinetic-openni2-launch
Requires:       ros-kinetic-pcl-conversions
Requires:       ros-kinetic-pcl-msgs
Requires:       ros-kinetic-pcl-ros
Requires:       ros-kinetic-robot-self-filter
Requires:       ros-kinetic-rosbag
Requires:       ros-kinetic-rosboost-cfg
Requires:       ros-kinetic-roscpp-tutorials
Requires:       ros-kinetic-rviz
Requires:       ros-kinetic-sensor-msgs
Requires:       ros-kinetic-std-msgs
Requires:       ros-kinetic-std-srvs
Requires:       ros-kinetic-stereo-msgs
Requires:       ros-kinetic-tf
Requires:       ros-kinetic-tf-conversions
Requires:       ros-kinetic-tf2-ros
Requires:       ros-kinetic-visualization-msgs
Requires:       yaml-cpp-devel
BuildRequires:  boost-devel
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-cv-bridge
BuildRequires:  ros-kinetic-diagnostic-msgs
BuildRequires:  ros-kinetic-diagnostic-updater
BuildRequires:  ros-kinetic-dynamic-reconfigure
BuildRequires:  ros-kinetic-eigen-conversions
BuildRequires:  ros-kinetic-geometry-msgs
BuildRequires:  ros-kinetic-image-geometry
BuildRequires:  ros-kinetic-image-transport
BuildRequires:  ros-kinetic-image-view2
BuildRequires:  ros-kinetic-interactive-markers
BuildRequires:  ros-kinetic-jsk-data
BuildRequires:  ros-kinetic-jsk-footstep-msgs
BuildRequires:  ros-kinetic-jsk-recognition-msgs
BuildRequires:  ros-kinetic-jsk-recognition-utils
BuildRequires:  ros-kinetic-jsk-tools
BuildRequires:  ros-kinetic-jsk-topic-tools
BuildRequires:  ros-kinetic-kdl-conversions
BuildRequires:  ros-kinetic-kdl-parser
BuildRequires:  ros-kinetic-laser-assembler
BuildRequires:  ros-kinetic-message-generation
BuildRequires:  ros-kinetic-moveit-core
BuildRequires:  ros-kinetic-moveit-ros-perception
BuildRequires:  ros-kinetic-nav-msgs
BuildRequires:  ros-kinetic-nodelet
BuildRequires:  ros-kinetic-octomap
BuildRequires:  ros-kinetic-octomap-msgs
BuildRequires:  ros-kinetic-octomap-ros
BuildRequires:  ros-kinetic-octomap-server
BuildRequires:  ros-kinetic-pcl-conversions
BuildRequires:  ros-kinetic-pcl-msgs
BuildRequires:  ros-kinetic-pcl-ros
BuildRequires:  ros-kinetic-robot-self-filter
BuildRequires:  ros-kinetic-rosboost-cfg
BuildRequires:  ros-kinetic-roscpp-tutorials
BuildRequires:  ros-kinetic-roslaunch
BuildRequires:  ros-kinetic-rostest
BuildRequires:  ros-kinetic-sensor-msgs
BuildRequires:  ros-kinetic-std-msgs
BuildRequires:  ros-kinetic-std-srvs
BuildRequires:  ros-kinetic-stereo-msgs
BuildRequires:  ros-kinetic-tf
BuildRequires:  ros-kinetic-tf-conversions
BuildRequires:  ros-kinetic-tf2-ros
BuildRequires:  ros-kinetic-visualization-msgs
BuildRequires:  yaml-cpp-devel

%description
jsk_pcl_ros

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Sat Mar 04 2017 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 1.1.1-0
- Autogenerated by Bloom

* Sun Feb 12 2017 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 1.1.0-2
- Autogenerated by Bloom

