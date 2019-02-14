Name:           ros-melodic-jsk-pcl-ros-utils
Version:        1.2.7
Release:        2%{?dist}
Summary:        ROS jsk_pcl_ros_utils package

Group:          Development/Libraries
License:        BSD
URL:            http://jsk-docs.readthedocs.io/en/latest/jsk_recognition/doc/jsk_pcl_ros_utils
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       python-scikit-learn
Requires:       ros-melodic-compressed-depth-image-transport
Requires:       ros-melodic-compressed-image-transport
Requires:       ros-melodic-cv-bridge
Requires:       ros-melodic-diagnostic-msgs
Requires:       ros-melodic-diagnostic-updater
Requires:       ros-melodic-dynamic-reconfigure
Requires:       ros-melodic-eigen-conversions
Requires:       ros-melodic-geometry-msgs
Requires:       ros-melodic-image-geometry
Requires:       ros-melodic-image-transport
Requires:       ros-melodic-image-view
Requires:       ros-melodic-image-view2
Requires:       ros-melodic-interactive-markers
Requires:       ros-melodic-jsk-data
Requires:       ros-melodic-jsk-footstep-msgs
Requires:       ros-melodic-jsk-recognition-msgs
Requires:       ros-melodic-jsk-recognition-utils
Requires:       ros-melodic-jsk-topic-tools
Requires:       ros-melodic-kdl-conversions
Requires:       ros-melodic-kdl-parser
Requires:       ros-melodic-laser-assembler
Requires:       ros-melodic-message-runtime
Requires:       ros-melodic-moveit-core
Requires:       ros-melodic-moveit-ros-perception
Requires:       ros-melodic-nav-msgs
Requires:       ros-melodic-nodelet
Requires:       ros-melodic-octomap
Requires:       ros-melodic-octomap-msgs
Requires:       ros-melodic-octomap-ros
Requires:       ros-melodic-octomap-server
Requires:       ros-melodic-openni2-launch
Requires:       ros-melodic-pcl-conversions
Requires:       ros-melodic-pcl-msgs
Requires:       ros-melodic-pcl-ros
Requires:       ros-melodic-robot-self-filter
Requires:       ros-melodic-rosbag
Requires:       ros-melodic-rosboost-cfg
Requires:       ros-melodic-roscpp-tutorials
Requires:       ros-melodic-rviz
Requires:       ros-melodic-sensor-msgs
Requires:       ros-melodic-std-msgs
Requires:       ros-melodic-std-srvs
Requires:       ros-melodic-stereo-msgs
Requires:       ros-melodic-tf
Requires:       ros-melodic-tf-conversions
Requires:       ros-melodic-tf2-ros
Requires:       ros-melodic-visualization-msgs
Requires:       yaml-cpp-devel
BuildRequires:  boost-devel
BuildRequires:  ros-melodic-catkin
BuildRequires:  ros-melodic-cv-bridge
BuildRequires:  ros-melodic-diagnostic-msgs
BuildRequires:  ros-melodic-diagnostic-updater
BuildRequires:  ros-melodic-dynamic-reconfigure
BuildRequires:  ros-melodic-eigen-conversions
BuildRequires:  ros-melodic-geometry-msgs
BuildRequires:  ros-melodic-image-geometry
BuildRequires:  ros-melodic-image-transport
BuildRequires:  ros-melodic-image-view2
BuildRequires:  ros-melodic-interactive-markers
BuildRequires:  ros-melodic-jsk-data
BuildRequires:  ros-melodic-jsk-footstep-msgs
BuildRequires:  ros-melodic-jsk-recognition-msgs
BuildRequires:  ros-melodic-jsk-recognition-utils
BuildRequires:  ros-melodic-jsk-tools
BuildRequires:  ros-melodic-jsk-topic-tools
BuildRequires:  ros-melodic-kdl-conversions
BuildRequires:  ros-melodic-kdl-parser
BuildRequires:  ros-melodic-laser-assembler
BuildRequires:  ros-melodic-message-generation
BuildRequires:  ros-melodic-moveit-core
BuildRequires:  ros-melodic-moveit-ros-perception
BuildRequires:  ros-melodic-nav-msgs
BuildRequires:  ros-melodic-nodelet
BuildRequires:  ros-melodic-octomap
BuildRequires:  ros-melodic-octomap-msgs
BuildRequires:  ros-melodic-octomap-ros
BuildRequires:  ros-melodic-octomap-server
BuildRequires:  ros-melodic-pcl-conversions
BuildRequires:  ros-melodic-pcl-msgs
BuildRequires:  ros-melodic-pcl-ros
BuildRequires:  ros-melodic-robot-self-filter
BuildRequires:  ros-melodic-rosboost-cfg
BuildRequires:  ros-melodic-roscpp-tutorials
BuildRequires:  ros-melodic-roslaunch
BuildRequires:  ros-melodic-rostest
BuildRequires:  ros-melodic-sensor-msgs
BuildRequires:  ros-melodic-std-msgs
BuildRequires:  ros-melodic-std-srvs
BuildRequires:  ros-melodic-stereo-msgs
BuildRequires:  ros-melodic-tf
BuildRequires:  ros-melodic-tf-conversions
BuildRequires:  ros-melodic-tf2-ros
BuildRequires:  ros-melodic-visualization-msgs
BuildRequires:  yaml-cpp-devel

%description
ROS utility nodelets for pointcloud perception.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/melodic

%changelog
* Thu Feb 14 2019 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 1.2.7-2
- Autogenerated by Bloom

