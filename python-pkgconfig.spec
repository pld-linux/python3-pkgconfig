#
# Conditional build:
%bcond_with	tests	# unit tests (not included in pypi release)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Python 2 interface to pkg-config
Summary(pl.UTF-8):	Interfejs Pythona 2 do narzędzia pkg-config
Name:		python-pkgconfig
# keep 1.5.2 here for python2 support
# (oficial support dropped in 1.5.4, but 1.5.3 has syntax errors under python2)
Version:	1.5.2
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pkgconfig/
Source0:	https://files.pythonhosted.org/packages/source/p/pkgconfig/pkgconfig-%{version}.tar.gz
# Source0-md5:	0d889edf670b644bfeaa3bb9444169cb
URL:		https://github.com/matze/pkgconfig
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-pytest >= 3.8.2
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.3
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-pytest >= 3.8.2
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pkgconfig is a Python module to interface with the pkg-config command
line tool.

%description -l pl.UTF-8
pkgconfig to moduł Pythona do współpracy z narzędziem linii poleceń
pkg-config.

%package -n python3-pkgconfig
Summary:	Python 3 interface to pkg-config
Summary(pl.UTF-8):	Interfejs Pythona 3 do narzędzia pkg-config
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.3

%description -n python3-pkgconfig
pkgconfig is a Python module to interface with the pkg-config command
line tool.

%description -n python3-pkgconfig -l pl.UTF-8
pkgconfig to moduł Pythona do współpracy z narzędziem linii poleceń
pkg-config.

%prep
%setup -q -n pkgconfig-%{version}

%build
%if %{with python2}
%py_build

%{?with_tests:%{__python} -m pytest test_pkgconfig.py}
%endif

%if %{with python3}
%py3_build

%{?with_tests:%{__python3} -m pytest test_pkgconfig.py}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py_sitescriptdir}/pkgconfig
%{py_sitescriptdir}/pkgconfig-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-pkgconfig
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/pkgconfig
%{py3_sitescriptdir}/pkgconfig-%{version}-py*.egg-info
%endif
