%define oname pyliblzma
%define module lzma

Summary:	Python bindings for the LZMA compression library
Name:		python-%{module}
Version:	0.5.3
Release:	10
License:	LGPLv2+
Group:		Development/Python
Url:		http://www.joachim-bauch.de/projects/python/pylzma
Source0:	http://www.joachim-bauch.de/projects/python/pylzma/releases/%{oname}-%{version}.tar.bz2
BuildRequires:	python2-distribute
BuildRequires:	pkgconfig(liblzma)
BuildRequires:	pkgconfig(python2)

%description
Python bindings for the LZMA compression library.

%package -n python2-%{module}
Summary:	Python 2 bindings for the LZMA compression library
%rename	%{oname}
%rename	python-liblzma
%rename	python-%{module}

%description -n python2-%{module}
Python 2 bindings for the LZMA compression library.

%prep
%setup -qn pyliblzma-%{version}

%build
env CFLAGS="%{optflags}" python2 setup.py build

%install
python2 setup.py install --root=%{buildroot} --record=INSTALLED_FILES
chmod +x %{buildroot}%{python2_sitearch}/liblzma.py

%files -n python2-%{module}
%doc README NEWS COPYING ChangeLog
%{python2_sitearch}/*.py*
%{python2_sitearch}/pyliblzma*.egg-info
%{python2_sitearch}/lzma.so

