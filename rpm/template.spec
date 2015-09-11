Name:           ros-hydro-jsk-recognition
Version:        0.3.6
Release:        0%{?dist}
Summary:        ROS jsk_recognition package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/jsk_recognition
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-hydro-checkerboard-detector
Requires:       ros-hydro-imagesift
Requires:       ros-hydro-jsk-pcl-ros
Requires:       ros-hydro-jsk-perception
Requires:       ros-hydro-jsk-recognition-msgs
Requires:       ros-hydro-jsk-recognition-utils
Requires:       ros-hydro-resized-image-transport
BuildRequires:  ros-hydro-catkin

%description
Metapackage that contains recognition package for jsk-ros-pkg

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
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
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Fri Sep 11 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.3.6-0
- Autogenerated by Bloom

* Wed Sep 09 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.3.5-0
- Autogenerated by Bloom

* Mon Sep 07 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.3.4-0
- Autogenerated by Bloom

* Sun Sep 06 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.3.3-0
- Autogenerated by Bloom

* Sat Sep 05 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.3.2-0
- Autogenerated by Bloom

* Fri Sep 04 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.3.1-0
- Autogenerated by Bloom

* Fri Sep 04 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.3.0-0
- Autogenerated by Bloom

* Fri Sep 04 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.2.18-0
- Autogenerated by Bloom

* Fri Aug 21 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.2.17-0
- Autogenerated by Bloom

* Wed Aug 19 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.2.16-0
- Autogenerated by Bloom

* Tue Aug 18 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.2.15-0
- Autogenerated by Bloom

* Fri Aug 14 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.2.14-0
- Autogenerated by Bloom

* Fri Jun 19 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.2.13-0
- Autogenerated by Bloom

* Mon May 04 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.2.12-0
- Autogenerated by Bloom

* Mon Apr 13 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.2.11-0
- Autogenerated by Bloom

* Thu Apr 09 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.2.10-0
- Autogenerated by Bloom

* Wed Apr 01 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.2.9-0
- Autogenerated by Bloom

* Thu Mar 26 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.2.7-0
- Autogenerated by Bloom

* Wed Mar 25 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.2.6-0
- Autogenerated by Bloom

* Tue Mar 17 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.2.5-0
- Autogenerated by Bloom

* Mon Mar 09 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.2.4-0
- Autogenerated by Bloom

* Mon Feb 02 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.2.3-0
- Autogenerated by Bloom

* Fri Jan 30 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.2.2-0
- Autogenerated by Bloom

* Fri Jan 30 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.2.1-0
- Autogenerated by Bloom

* Thu Jan 29 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.2.0-0
- Autogenerated by Bloom

* Sat Jan 24 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.1.33-0
- Autogenerated by Bloom

* Mon Jan 12 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.1.32-0
- Autogenerated by Bloom

* Thu Jan 08 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.1.31-0
- Autogenerated by Bloom

* Wed Dec 24 2014 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.1.30-0
- Autogenerated by Bloom

* Wed Dec 24 2014 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.1.29-0
- Autogenerated by Bloom

* Sun Dec 21 2014 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.1.28-0
- Autogenerated by Bloom

* Tue Dec 09 2014 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.1.27-0
- Autogenerated by Bloom

* Sun Nov 23 2014 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.1.26-0
- Autogenerated by Bloom

* Sat Nov 22 2014 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.1.25-0
- Autogenerated by Bloom

