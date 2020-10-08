%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-jsk-perception
Version:        1.2.13
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS jsk_perception package

License:        BSD
URL:            https://jsk-docs.readthedocs.io/projects/jsk_recognition/en/latest/jsk_perception
Source0:        %{name}-%{version}.tar.gz

Requires:       eigen3-devel
Requires:       leveldb-devel
Requires:       python3-PyYAML
Requires:       python3-h5py
Requires:       python3-scikit-learn
Requires:       ros-noetic-angles
Requires:       ros-noetic-checkerboard-detector
Requires:       ros-noetic-cv-bridge
Requires:       ros-noetic-dynamic-reconfigure
Requires:       ros-noetic-geometry-msgs
Requires:       ros-noetic-image-geometry
Requires:       ros-noetic-image-transport
Requires:       ros-noetic-image-view
Requires:       ros-noetic-image-view2
Requires:       ros-noetic-imagesift
Requires:       ros-noetic-jsk-data
Requires:       ros-noetic-jsk-gui-msgs
Requires:       ros-noetic-jsk-recognition-msgs
Requires:       ros-noetic-jsk-recognition-utils
Requires:       ros-noetic-jsk-topic-tools
Requires:       ros-noetic-libcmt
Requires:       ros-noetic-message-runtime
Requires:       ros-noetic-mk
Requires:       ros-noetic-nodelet
Requires:       ros-noetic-opencv-apps
Requires:       ros-noetic-openni2-launch
Requires:       ros-noetic-pcl-ros
Requires:       ros-noetic-posedetection-msgs
Requires:       ros-noetic-robot-self-filter
Requires:       ros-noetic-rosbag
Requires:       ros-noetic-roscpp
Requires:       ros-noetic-rospack
Requires:       ros-noetic-rospy
Requires:       ros-noetic-rostopic
Requires:       ros-noetic-rqt-gui
Requires:       ros-noetic-rviz
Requires:       ros-noetic-sensor-msgs
Requires:       ros-noetic-sound-play
Requires:       ros-noetic-std-msgs
Requires:       ros-noetic-tf
Requires:       ros-noetic-tf2-geometry-msgs
Requires:       ros-noetic-topic-tools
Requires:       yaml-cpp-devel
BuildRequires:  eigen3-devel
BuildRequires:  git
BuildRequires:  ros-noetic-angles
BuildRequires:  ros-noetic-catkin
BuildRequires:  ros-noetic-cmake-modules
BuildRequires:  ros-noetic-cv-bridge
BuildRequires:  ros-noetic-dynamic-reconfigure
BuildRequires:  ros-noetic-geometry-msgs
BuildRequires:  ros-noetic-image-geometry
BuildRequires:  ros-noetic-image-transport
BuildRequires:  ros-noetic-image-view2
BuildRequires:  ros-noetic-jsk-data
BuildRequires:  ros-noetic-jsk-recognition-msgs
BuildRequires:  ros-noetic-jsk-recognition-utils
BuildRequires:  ros-noetic-jsk-tools
BuildRequires:  ros-noetic-jsk-topic-tools
BuildRequires:  ros-noetic-libcmt
BuildRequires:  ros-noetic-message-generation
BuildRequires:  ros-noetic-mk
BuildRequires:  ros-noetic-nodelet
BuildRequires:  ros-noetic-opencv-apps
BuildRequires:  ros-noetic-pcl-ros
BuildRequires:  ros-noetic-posedetection-msgs
BuildRequires:  ros-noetic-robot-self-filter
BuildRequires:  ros-noetic-roscpp
BuildRequires:  ros-noetic-roslaunch
BuildRequires:  ros-noetic-roslint
BuildRequires:  ros-noetic-rospack
BuildRequires:  ros-noetic-rostest
BuildRequires:  ros-noetic-sensor-msgs
BuildRequires:  ros-noetic-std-msgs
BuildRequires:  ros-noetic-tf
BuildRequires:  yaml-cpp-devel
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
ROS nodes and nodelets for 2-D image perception.

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
* Thu Oct 08 2020 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.2.13-1
- Autogenerated by Bloom

* Sun Oct 04 2020 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.2.12-1
- Autogenerated by Bloom

* Thu Oct 01 2020 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.2.11-1
- Autogenerated by Bloom

