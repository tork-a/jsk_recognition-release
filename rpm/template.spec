Name:           ros-indigo-imagesift
Version:        0.3.23
Release:        0%{?dist}
Summary:        ROS imagesift package

Group:          Development/Libraries
License:        LGPL
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-cv-bridge
Requires:       ros-indigo-image-transport
Requires:       ros-indigo-jsk-recognition-utils
Requires:       ros-indigo-libsiftfast
Requires:       ros-indigo-nodelet
Requires:       ros-indigo-posedetection-msgs
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-sensor-msgs
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-cmake-modules
BuildRequires:  ros-indigo-cv-bridge
BuildRequires:  ros-indigo-image-transport
BuildRequires:  ros-indigo-jsk-recognition-utils
BuildRequires:  ros-indigo-libsiftfast
BuildRequires:  ros-indigo-nodelet
BuildRequires:  ros-indigo-posedetection-msgs
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-sensor-msgs

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
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Wed Sep 14 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 0.3.23-0
- Autogenerated by Bloom

* Tue Sep 13 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 0.3.22-0
- Autogenerated by Bloom

* Fri Apr 15 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 0.3.21-0
- Autogenerated by Bloom

* Thu Apr 14 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 0.3.20-0
- Autogenerated by Bloom

* Tue Mar 22 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 0.3.19-0
- Autogenerated by Bloom

* Mon Mar 21 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 0.3.18-0
- Autogenerated by Bloom

* Sun Mar 20 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 0.3.17-0
- Autogenerated by Bloom

* Thu Feb 11 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 0.3.16-0
- Autogenerated by Bloom

* Tue Feb 09 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 0.3.15-0
- Autogenerated by Bloom

* Fri Feb 05 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 0.3.14-0
- Autogenerated by Bloom

* Sun Dec 20 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 0.3.13-1
- Autogenerated by Bloom

* Sun Dec 20 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 0.3.13-0
- Autogenerated by Bloom

* Fri Dec 18 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 0.3.11-0
- Autogenerated by Bloom

* Thu Dec 17 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 0.3.10-0
- Autogenerated by Bloom

* Wed Dec 16 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 0.3.9-0
- Autogenerated by Bloom

* Fri Dec 11 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 0.3.8-1
- Autogenerated by Bloom

* Fri Sep 11 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 0.3.6-0
- Autogenerated by Bloom

* Wed Sep 09 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 0.3.5-0
- Autogenerated by Bloom

* Mon Sep 07 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 0.3.4-0
- Autogenerated by Bloom

* Sun Sep 06 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 0.3.3-0
- Autogenerated by Bloom

* Sat Sep 05 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 0.3.2-0
- Autogenerated by Bloom

* Fri Sep 04 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 0.3.1-0
- Autogenerated by Bloom

* Fri Sep 04 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 0.3.0-0
- Autogenerated by Bloom

* Fri Sep 04 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 0.2.18-0
- Autogenerated by Bloom

* Fri Aug 21 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 0.2.17-0
- Autogenerated by Bloom

* Wed Aug 19 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 0.2.16-0
- Autogenerated by Bloom

* Tue Aug 18 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 0.2.15-0
- Autogenerated by Bloom

* Fri Aug 14 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 0.2.14-0
- Autogenerated by Bloom

* Fri Jun 19 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 0.2.13-0
- Autogenerated by Bloom

* Mon May 04 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 0.2.12-0
- Autogenerated by Bloom

* Mon Apr 13 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 0.2.11-0
- Autogenerated by Bloom

* Thu Apr 09 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 0.2.10-0
- Autogenerated by Bloom

* Wed Apr 01 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 0.2.9-0
- Autogenerated by Bloom

* Thu Mar 26 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 0.2.7-0
- Autogenerated by Bloom

* Wed Mar 25 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 0.2.6-0
- Autogenerated by Bloom

* Tue Mar 17 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 0.2.5-0
- Autogenerated by Bloom

* Mon Mar 09 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 0.2.4-0
- Autogenerated by Bloom

* Mon Feb 02 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 0.2.3-0
- Autogenerated by Bloom

* Fri Jan 30 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 0.2.2-0
- Autogenerated by Bloom

* Fri Jan 30 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 0.2.1-0
- Autogenerated by Bloom

* Thu Jan 29 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 0.2.0-0
- Autogenerated by Bloom

