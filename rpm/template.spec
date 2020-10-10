%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-imagesift
Version:        1.2.15
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS imagesift package

License:        LGPL
URL:            https://jsk-docs.readthedocs.io/projects/jsk_recognition/en/latest/imagesift
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-noetic-cv-bridge
Requires:       ros-noetic-image-transport
Requires:       ros-noetic-jsk-recognition-utils
Requires:       ros-noetic-jsk-topic-tools >= 2.2.8
Requires:       ros-noetic-libsiftfast
Requires:       ros-noetic-nodelet
Requires:       ros-noetic-posedetection-msgs
Requires:       ros-noetic-roscpp
Requires:       ros-noetic-sensor-msgs
BuildRequires:  python3-setuptools
BuildRequires:  ros-noetic-catkin
BuildRequires:  ros-noetic-cmake-modules
BuildRequires:  ros-noetic-cv-bridge
BuildRequires:  ros-noetic-image-transport
BuildRequires:  ros-noetic-jsk-recognition-utils
BuildRequires:  ros-noetic-jsk-topic-tools >= 2.2.8
BuildRequires:  ros-noetic-libsiftfast
BuildRequires:  ros-noetic-nodelet
BuildRequires:  ros-noetic-posedetection-msgs
BuildRequires:  ros-noetic-roscpp
BuildRequires:  ros-noetic-rostest
BuildRequires:  ros-noetic-sensor-msgs
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
For every image, computes its sift features and send a new message with the
image, its intrinsic parameters, and the features. Parameters include: display -
shows the image on the local computer

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
* Sat Oct 10 2020 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.2.15-1
- Autogenerated by Bloom

* Fri Oct 09 2020 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.2.14-1
- Autogenerated by Bloom

* Thu Oct 08 2020 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.2.13-1
- Autogenerated by Bloom

* Sun Oct 04 2020 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.2.12-1
- Autogenerated by Bloom

* Thu Oct 01 2020 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.2.11-1
- Autogenerated by Bloom

