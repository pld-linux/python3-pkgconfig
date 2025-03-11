#
# Conditional build:
%bcond_with	tests	# unit tests (not included in pypi release)

Summary:	Python 3 interface to pkg-config
Summary(pl.UTF-8):	Interfejs Pythona 3 do narzędzia pkg-config
Name:		python3-pkgconfig
Version:	1.5.5
Release:	3
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pkgconfig/
Source0:	https://files.pythonhosted.org/packages/source/p/pkgconfig/pkgconfig-%{version}.tar.gz
# Source0-md5:	12523e11b91b050ca49975cc033689a4
URL:		https://github.com/matze/pkgconfig
BuildRequires:	python3-modules >= 1:3.3
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-pytest >= 3.8.2
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pkgconfig is a Python module to interface with the pkg-config command
line tool.

%description -l pl.UTF-8
pkgconfig to moduł Pythona do współpracy z narzędziem linii poleceń
pkg-config.

%prep
%setup -q -n pkgconfig-%{version}

%build
%py3_build

%{?with_tests:%{__python3} -m pytest test_pkgconfig.py}

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/pkgconfig
%{py3_sitescriptdir}/pkgconfig-%{version}-py*.egg-info
