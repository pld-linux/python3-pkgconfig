#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Python 2 interface to pkg-config
Summary(pl.UTF-8):	Interfejs Pythona 2 do narzędzia pkg-config
Name:		python-pkgconfig
Version:	1.2.2
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.python.org/simple/pkgconfig
Source0:	https://files.pythonhosted.org/packages/source/p/pkgconfig/pkgconfig-%{version}.tar.gz
# Source0-md5:	81a8f6ef3371831d081e03db39e09683
URL:		http://github.com/matze/pkgconfig
%if %{with python2}
BuildRequires:	python-modules >= 1:2.6
BuildRequires:	python-nose >= 1.0
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-nose >= 1.0
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.6
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
Requires:	python3-modules >= 1:3.2

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

%{?with_tests:%{__python} -m nose test.py}
%endif

%if %{with python3}
%py3_build

%{?with_tests:%{__python3} -m nose test.py}
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
