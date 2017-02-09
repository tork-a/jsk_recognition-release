Name:           ros-jade-jsk-recognition
Version:        1.1.0
Release:        0%{?dist}
Summary:        ROS jsk_recognition package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/jsk_recognition
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-jade-checkerboard-detector
Requires:       ros-jade-imagesift
Requires:       ros-jade-jsk-pcl-ros
Requires:       ros-jade-jsk-perception
Requires:       ros-jade-jsk-recognition-msgs
Requires:       ros-jade-jsk-recognition-utils
Requires:       ros-jade-resized-image-transport
BuildRequires:  ros-jade-catkin

%description
Metapackage that contains recognition package for jsk-ros-pkg

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
        -DCMAKE_INSTALL_LIBDIR="lib" \
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
* Thu Feb 09 2017 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 1.1.0-0
- Autogenerated by Bloom

* Tue Nov 22 2016 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.3.29-0
- Autogenerated by Bloom

* Sat Oct 29 2016 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.3.28-0
- Autogenerated by Bloom

* Fri Sep 16 2016 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.3.25-0
- Autogenerated by Bloom

* Thu Sep 15 2016 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.3.24-0
- Autogenerated by Bloom

* Wed Sep 14 2016 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.3.23-0
- Autogenerated by Bloom

* Tue Sep 13 2016 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.3.22-0
- Autogenerated by Bloom

* Fri Apr 15 2016 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.3.21-0
- Autogenerated by Bloom

* Thu Apr 14 2016 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.3.20-0
- Autogenerated by Bloom

* Tue Mar 22 2016 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.3.19-0
- Autogenerated by Bloom

* Mon Mar 21 2016 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.3.18-0
- Autogenerated by Bloom

* Sun Mar 20 2016 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.3.17-0
- Autogenerated by Bloom

* Thu Feb 11 2016 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.3.16-0
- Autogenerated by Bloom

* Tue Feb 09 2016 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.3.15-1
- Autogenerated by Bloom

* Tue Feb 09 2016 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.3.15-0
- Autogenerated by Bloom

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

* Fri Dec 18 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.3.11-0
- Autogenerated by Bloom

* Fri Dec 11 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.3.8-1
- Autogenerated by Bloom

