%global commit 86e8d9c173633f80d71250515a296c9c2b62f016
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global owner stadar
%global project trackpoint_pi
%global plugin trackpoint

Name: opencpn-plugin-%{plugin}
Summary: Trackpoint plugin for OpenCPN
Version: 0.2
Release: 1.%{shortcommit}%{?dist}
License: GPLv2+

Source0: https://github.com/%{owner}/%{project}/archive/%{commit}/%{project}-%{shortcommit}.tar.gz

BuildRequires: bzip2-devel
BuildRequires: cmake
BuildRequires: gettext
BuildRequires: tinyxml-devel
BuildRequires: wxGTK3-devel
BuildRequires: zlib-devel

Requires: opencpn%{_isa}
Enhances: opencpn%{_isa}

%description
Plugin that adds ORE 4410D-01 TRACKPOINT II Plus SYSTEM target data to OpenCPN.

%prep
%autosetup -n %{project}-%{commit}

sed -i -e s'/SET(PREFIX_LIB lib)/SET(PREFIX_LIB %{_lib})/' cmake/PluginInstall.cmake

mkdir build

%build

cd build
%cmake -DBUILD_SHARED_LIBS:BOOL=OFF ..
%make_build

%install

cd build
mkdir -p %{buildroot}%{_bindir}
%make_install

%files

%{_libdir}/opencpn/lib%{plugin}_pi.so
