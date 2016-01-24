Name:           ros-jade-checkerboard-detector
Version:        0.3.13
Release:        8%{?dist}
Summary:        ROS checkerboard_detector package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-jade-cv-bridge
Requires:       ros-jade-dynamic-tf-publisher
Requires:       ros-jade-eigen-conversions
Requires:       ros-jade-image-geometry
Requires:       ros-jade-jsk-recognition-msgs
Requires:       ros-jade-message-filters
Requires:       ros-jade-posedetection-msgs
Requires:       ros-jade-rosconsole
Requires:       ros-jade-roscpp
Requires:       ros-jade-sensor-msgs
Requires:       ros-jade-tf
Requires:       ros-jade-tf2
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-cv-bridge
BuildRequires:  ros-jade-eigen-conversions
BuildRequires:  ros-jade-image-geometry
BuildRequires:  ros-jade-jsk-recognition-msgs
BuildRequires:  ros-jade-message-filters
BuildRequires:  ros-jade-posedetection-msgs
BuildRequires:  ros-jade-rosconsole
BuildRequires:  ros-jade-roscpp
BuildRequires:  ros-jade-sensor-msgs
BuildRequires:  ros-jade-tf
BuildRequires:  ros-jade-tf2

%description
Uses opencv to find checkboards and compute their 6D poses with respect to the
image. Requires the image to be calibrated. Parameters: display - show the
checkerboard detection rect%d_size_x - size of checker in x direction
rect%d_size_y - size of checker in y direction grid%d_size_x - number of
checkers in x direction grid%d_size_y - number of checkers in y direction There
can be more than one grid%d declared, the numbers should grow consecutively
starting at 0.

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

