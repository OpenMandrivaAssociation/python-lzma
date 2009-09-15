%define oname pylzma
%define module lzma

Summary:	Python bindings for the LZMA compression library
Name:		python-%{module}
Version:	0.3.0
Release:	%mkrel 8
License:	LGPLv2+
Group:		Development/Python
Url:		http://www.joachim-bauch.de/projects/python/pylzma
Source0:	http://www.joachim-bauch.de/projects/python/pylzma/releases/%{oname}-%{version}.tar.bz2
%py_requires -d
Provides:	%{oname}
Obsoletes:	%{oname}
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Python bindings for the LZMA compression library.

%prep
%setup -qn %{oname}-%{version}

%build
env CFLAGS="%{optflags}" python setup.py build

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

python setup.py install --root=%{buildroot} --record=INSTALLED_FILES

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc readme.txt doc/*
%{python_sitearch}/*.py*
%{python_sitearch}/%{oname}*.egg-info
%{python_sitearch}/%{oname}.so
