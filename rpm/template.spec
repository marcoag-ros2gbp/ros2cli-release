%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/rolling/.*$
%global __requires_exclude_from ^/opt/ros/rolling/.*$

Name:           ros-rolling-ros2lifecycle
Version:        0.28.0
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS ros2lifecycle package

License:        Apache License 2.0
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-rolling-lifecycle-msgs
Requires:       ros-rolling-rclpy
Requires:       ros-rolling-ros2cli
Requires:       ros-rolling-ros2node
Requires:       ros-rolling-ros2service
Requires:       ros-rolling-ros-workspace
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  ros-rolling-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-pytest-timeout
BuildRequires:  ros-rolling-ament-copyright
BuildRequires:  ros-rolling-ament-flake8
BuildRequires:  ros-rolling-ament-pep257
BuildRequires:  ros-rolling-ament-xmllint
BuildRequires:  ros-rolling-launch
BuildRequires:  ros-rolling-launch-ros
BuildRequires:  ros-rolling-launch-testing
BuildRequires:  ros-rolling-launch-testing-ros
BuildRequires:  ros-rolling-ros2lifecycle-test-fixtures
%endif

%description
The lifecycle command for ROS 2 command line tools.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%py3_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%py3_install -- --prefix "/opt/ros/rolling"

%if 0%{?with_tests}
%check
# Look for a directory with a name indicating that it contains tests
TEST_TARGET=$(ls -d * | grep -m1 "\(test\|tests\)" ||:)
if [ -n "$TEST_TARGET" ] && %__python3 -m pytest --version; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%__python3 -m pytest $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/rolling

%changelog
* Tue Jul 11 2023 Audrow Nash <audrow@openrobotics.org> - 0.28.0-1
- Autogenerated by Bloom

* Wed Jun 07 2023 Audrow Nash <audrow@openrobotics.org> - 0.27.0-1
- Autogenerated by Bloom

* Thu May 11 2023 Audrow Nash <audrow@openrobotics.org> - 0.26.1-1
- Autogenerated by Bloom

* Fri Apr 28 2023 Audrow Nash <audrow@openrobotics.org> - 0.26.0-1
- Autogenerated by Bloom

* Tue Apr 18 2023 Audrow Nash <audrow@openrobotics.org> - 0.25.0-1
- Autogenerated by Bloom

* Wed Apr 12 2023 Audrow Nash <audrow@openrobotics.org> - 0.24.1-1
- Autogenerated by Bloom

* Tue Apr 11 2023 Audrow Nash <audrow@openrobotics.org> - 0.24.0-1
- Autogenerated by Bloom

* Tue Mar 21 2023 Audrow Nash <audrow@openrobotics.org> - 0.23.0-2
- Autogenerated by Bloom

