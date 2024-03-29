# Disable debug package
%define debug_package %{nil}

Name:          hwc
Version:       %{_rpm_version}
Release:       1%{?dist}%{?_rpm_branch}
Summary:       Hello World on C
License:       Proprietary
Source0:       %{name}-%{_rpm_version}.tar.gz
BuildRoot:     %{_tmppath}/%{name}-%{_rpm_version}-%{release}-root-%(%{__id_u} -n)
Provides:      hwcpp = %{_rpm_version}-%{release}

%description
A simple Hello World project on pure C

%prep
%setup -q

%build
make

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf "$RPM_BUILD_ROOT"

%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf "$RPM_BUILD_ROOT"
mkdir -p $RPM_BUILD_ROOT%{_bindir}
make install DESTDIR="$RPM_BUILD_ROOT"

%files
%defattr(0755,root,root,0755)
%{_bindir}/hwc

%changelog
* Thu Aug 05 2019 Alexey Ankudinov <lex@autumn.su> - 1.0.0
- First release
