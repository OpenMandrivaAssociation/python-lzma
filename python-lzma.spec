%define oname pyliblzma
%define module lzma

Summary:	Python bindings for the LZMA compression library
Name:		python-%{module}
Version:	0.5.3
Release:	4
License:	LGPLv2+
Group:		Development/Python
Url:		http://www.joachim-bauch.de/projects/python/pylzma
Source0:	http://www.joachim-bauch.de/projects/python/pylzma/releases/%{oname}-%{version}.tar.bz2
BuildRequires:	python-setuptools
BuildRequires:	pkgconfig(liblzma)
BuildRequires:	pkgconfig(python)
%rename	%{oname}
%rename	python-liblzma

%description
Python bindings for the LZMA compression library.

%prep
%setup -qn pyliblzma-%{version}

%build
env CFLAGS="%{optflags}" python setup.py build

%install
python setup.py install --root=%{buildroot} --record=INSTALLED_FILES

%files
%doc README NEWS COPYING ChangeLog
%{python_sitearch}/*.py*
%{python_sitearch}/pyliblzma*.egg-info
%{python_sitearch}/lzma.so

