#
# spec file for package monitoring-check_ro_mounts
#

Name:           monitoring-check_ro_mounts
Version:        %{version}
Release:        %{release}
Summary:        Check read only filesystem mounts
License:        GPLv2
Group:          System/Monitoring
Url:            https://github.com/joernott/monitoring-check_ro_mounts
Source0:        monitoring-check_ro_mounts-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl
Provides:       check_ro_mounts

%description
This plugin checks the mount table for read-only mounts - these are usually a sign of
trouble (broken filesystem etc).

%prep
%setup -q -n monitoring-check_ro_mounts-%{version}

%install
mkdir -p "$RPM_BUILD_ROOT/usr/lib64/nagios/plugins"
cp check_ro_mounts "$RPM_BUILD_ROOT/usr/lib64/nagios/plugins/"

%files
%defattr(-,root,root,755)
%attr(0755,root,root) /usr/lib64/nagios/plugins/check_ro_mounts

%changelog
* Thu Apr 28 2022 Joern Ott <joern.ott@ott-consult.de>
- Add rpm build script and SPEC file

