Name:           ros-melodic-jsk-recognition-utils
Version:        1.2.7
Release:        2%{?dist}
Summary:        ROS jsk_recognition_utils package

Group:          Development/Libraries
License:        BSD
URL:            http://jsk-docs.readthedocs.io/en/latest/jsk_recognition/jsk_recognition_utils
Source0:        %{name}-%{version}.tar.gz

Requires:       python-scikit-image
Requires:       ros-melodic-eigen-conversions
Requires:       ros-melodic-geometry-msgs
Requires:       ros-melodic-image-geometry
Requires:       ros-melodic-jsk-recognition-msgs
Requires:       ros-melodic-jsk-topic-tools
Requires:       ros-melodic-message-runtime
Requires:       ros-melodic-pcl-msgs
Requires:       ros-melodic-pcl-ros
Requires:       ros-melodic-sensor-msgs
Requires:       ros-melodic-std-msgs
Requires:       ros-melodic-tf
Requires:       ros-melodic-tf-conversions
Requires:       ros-melodic-tf2-ros
Requires:       ros-melodic-visualization-msgs
Requires:       yaml-cpp-devel
BuildRequires:  Cython
BuildRequires:  ros-melodic-catkin
BuildRequires:  ros-melodic-dynamic-reconfigure
BuildRequires:  ros-melodic-eigen-conversions
BuildRequires:  ros-melodic-geometry-msgs
BuildRequires:  ros-melodic-image-geometry
BuildRequires:  ros-melodic-jsk-recognition-msgs
BuildRequires:  ros-melodic-jsk-tools
BuildRequires:  ros-melodic-jsk-topic-tools
BuildRequires:  ros-melodic-message-generation
BuildRequires:  ros-melodic-pcl-msgs
BuildRequires:  ros-melodic-pcl-ros
BuildRequires:  ros-melodic-sensor-msgs
BuildRequires:  ros-melodic-std-msgs
BuildRequires:  ros-melodic-tf
BuildRequires:  ros-melodic-tf-conversions
BuildRequires:  ros-melodic-tf2-ros
BuildRequires:  ros-melodic-visualization-msgs
BuildRequires:  yaml-cpp-devel

%description
C++ library about sensor model, geometrical modeling and perception.

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

