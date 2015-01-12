Name:           ros-hydro-imagesift
Version:        0.1.32
Release:        0%{?dist}
Summary:        ROS imagesift package

Group:          Development/Libraries
License:        LGPL
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-hydro-cv-bridge
Requires:       ros-hydro-image-transport
Requires:       ros-hydro-libsiftfast
Requires:       ros-hydro-posedetection-msgs
Requires:       ros-hydro-roscpp
Requires:       ros-hydro-sensor-msgs
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-cv-bridge
BuildRequires:  ros-hydro-image-transport
BuildRequires:  ros-hydro-libsiftfast
BuildRequires:  ros-hydro-posedetection-msgs
BuildRequires:  ros-hydro-roscpp
BuildRequires:  ros-hydro-sensor-msgs

%description
For every image, computes its sift features and send a new message with the
image, its intrinsic parameters, and the features. Parameters include: display -
shows the image on the local computer

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p build && cd build
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
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Mon Jan 12 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 0.1.32-0
- Autogenerated by Bloom

* Thu Jan 08 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 0.1.31-0
- Autogenerated by Bloom

* Wed Dec 24 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 0.1.30-0
- Autogenerated by Bloom

* Wed Dec 24 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 0.1.29-0
- Autogenerated by Bloom

* Sun Dec 21 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 0.1.28-0
- Autogenerated by Bloom

* Tue Dec 09 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 0.1.27-0
- Autogenerated by Bloom

* Sun Nov 23 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 0.1.26-0
- Autogenerated by Bloom

* Sat Nov 22 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 0.1.25-0
- Autogenerated by Bloom

