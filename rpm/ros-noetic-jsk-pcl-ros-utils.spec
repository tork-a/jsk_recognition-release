%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-jsk-pcl-ros-utils
Version:        1.2.11
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS jsk_pcl_ros_utils package

License:        BSD
URL:            https://jsk-docs.readthedocs.io/projects/jsk_recognition/en/latest/jsk_pcl_ros_utils
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       boost-python3-devel
Requires:       python3-scikit-learn
Requires:       ros-noetic-compressed-depth-image-transport
Requires:       ros-noetic-compressed-image-transport
Requires:       ros-noetic-cv-bridge
Requires:       ros-noetic-diagnostic-msgs
Requires:       ros-noetic-diagnostic-updater
Requires:       ros-noetic-dynamic-reconfigure
Requires:       ros-noetic-eigen-conversions
Requires:       ros-noetic-geometry-msgs
Requires:       ros-noetic-image-geometry
Requires:       ros-noetic-image-transport
Requires:       ros-noetic-image-view
Requires:       ros-noetic-image-view2
Requires:       ros-noetic-interactive-markers
Requires:       ros-noetic-jsk-data
Requires:       ros-noetic-jsk-footstep-msgs
Requires:       ros-noetic-jsk-recognition-msgs
Requires:       ros-noetic-jsk-recognition-utils
Requires:       ros-noetic-jsk-topic-tools
Requires:       ros-noetic-kdl-conversions
Requires:       ros-noetic-kdl-parser
Requires:       ros-noetic-laser-assembler
Requires:       ros-noetic-message-runtime
Requires:       ros-noetic-moveit-core
Requires:       ros-noetic-moveit-ros-perception
Requires:       ros-noetic-nav-msgs
Requires:       ros-noetic-nodelet
Requires:       ros-noetic-octomap
Requires:       ros-noetic-octomap-msgs
Requires:       ros-noetic-octomap-ros
Requires:       ros-noetic-octomap-server
Requires:       ros-noetic-openni2-launch
Requires:       ros-noetic-pcl-conversions
Requires:       ros-noetic-pcl-msgs
Requires:       ros-noetic-pcl-ros
Requires:       ros-noetic-robot-self-filter
Requires:       ros-noetic-rosbag
Requires:       ros-noetic-rosboost-cfg
Requires:       ros-noetic-roscpp-tutorials
Requires:       ros-noetic-rviz
Requires:       ros-noetic-sensor-msgs
Requires:       ros-noetic-std-msgs
Requires:       ros-noetic-std-srvs
Requires:       ros-noetic-stereo-msgs
Requires:       ros-noetic-tf
Requires:       ros-noetic-tf-conversions
Requires:       ros-noetic-tf2-ros
Requires:       ros-noetic-visualization-msgs
Requires:       yaml-cpp-devel
BuildRequires:  boost-devel
BuildRequires:  boost-python3-devel
BuildRequires:  python3-PyYAML
BuildRequires:  ros-noetic-catkin
BuildRequires:  ros-noetic-cv-bridge
BuildRequires:  ros-noetic-diagnostic-msgs
BuildRequires:  ros-noetic-diagnostic-updater
BuildRequires:  ros-noetic-dynamic-reconfigure
BuildRequires:  ros-noetic-eigen-conversions
BuildRequires:  ros-noetic-geometry-msgs
BuildRequires:  ros-noetic-image-geometry
BuildRequires:  ros-noetic-image-transport
BuildRequires:  ros-noetic-image-view2
BuildRequires:  ros-noetic-interactive-markers
BuildRequires:  ros-noetic-jsk-data
BuildRequires:  ros-noetic-jsk-footstep-msgs
BuildRequires:  ros-noetic-jsk-recognition-msgs
BuildRequires:  ros-noetic-jsk-recognition-utils
BuildRequires:  ros-noetic-jsk-tools
BuildRequires:  ros-noetic-jsk-topic-tools
BuildRequires:  ros-noetic-kdl-conversions
BuildRequires:  ros-noetic-kdl-parser
BuildRequires:  ros-noetic-laser-assembler
BuildRequires:  ros-noetic-message-generation
BuildRequires:  ros-noetic-moveit-core
BuildRequires:  ros-noetic-moveit-ros-perception
BuildRequires:  ros-noetic-nav-msgs
BuildRequires:  ros-noetic-nodelet
BuildRequires:  ros-noetic-octomap
BuildRequires:  ros-noetic-octomap-msgs
BuildRequires:  ros-noetic-octomap-ros
BuildRequires:  ros-noetic-octomap-server
BuildRequires:  ros-noetic-pcl-conversions
BuildRequires:  ros-noetic-pcl-msgs
BuildRequires:  ros-noetic-pcl-ros
BuildRequires:  ros-noetic-robot-self-filter
BuildRequires:  ros-noetic-rosboost-cfg
BuildRequires:  ros-noetic-roscpp-tutorials
BuildRequires:  ros-noetic-roslaunch
BuildRequires:  ros-noetic-rostest
BuildRequires:  ros-noetic-sensor-msgs
BuildRequires:  ros-noetic-std-msgs
BuildRequires:  ros-noetic-std-srvs
BuildRequires:  ros-noetic-stereo-msgs
BuildRequires:  ros-noetic-tf
BuildRequires:  ros-noetic-tf-conversions
BuildRequires:  ros-noetic-tf2-ros
BuildRequires:  ros-noetic-visualization-msgs
BuildRequires:  yaml-cpp-devel
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
ROS utility nodelets for pointcloud perception.

%prep
%autosetup

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_LIBDIR="lib" \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/noetic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/noetic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    -DCATKIN_BUILD_BINARY_PACKAGE="1" \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%files
/opt/ros/noetic

%changelog
* Thu Oct 01 2020 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 1.2.11-1
- Autogenerated by Bloom

