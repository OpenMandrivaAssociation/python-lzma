Summary:	Python bindings for the LZMA compression library
Name:		pylzma
Version:	0.3.0
Release:	%mkrel 1
License:	GPL
Group:		Development/Python
Url:		http://www.joachim-bauch.de/projects/python/pylzma
Source0:	http://www.joachim-bauch.de/projects/python/pylzma/releases/%{name}-%{version}.tar.bz2
%py_requires -d
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Python bindings for the LZMA compression library.

%prep
%setup -q

%build
env CFLAGS="%{optflags}" python setup.py build

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

python setup.py install --root=%{buildroot} --record=INSTALLED_FILES

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc
%attr(755,root,root)
%{python_sitearch}/*.py*
%{python_sitearch}/%{name}*.egg-info
%{python_sitearch}/%{name}.so
