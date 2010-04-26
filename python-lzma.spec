%define oname pylzma
%define module lzma

Summary:	Python bindings for the LZMA compression library
Name:		python-%{module}
Version:	0.5.2
Release:	%mkrel 1
License:	LGPLv2+
Group:		Development/Python
Url:		http://www.joachim-bauch.de/projects/python/pylzma
Source0:	http://www.joachim-bauch.de/projects/python/pylzma/releases/%{oname}-%{version}.tar.gz
%py_requires -d
BuildRequires:  python-setuptools
Provides:	%{oname}
Obsoletes:	%{oname}
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Python bindings for the LZMA compression library.

%prep
%setup -qn pyliblzma-%{version}

%build
env CFLAGS="%{optflags}" python setup.py build

%install
rm -rf %{buildroot}

python setup.py install --root=%{buildroot} --record=INSTALLED_FILES

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README NEWS COPYING ChangeLog
%{python_sitearch}/*.py*
%{python_sitearch}/pyliblzma*.egg-info
%{python_sitearch}/lzma.so
