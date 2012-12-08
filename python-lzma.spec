%define oname pyliblzma
%define module lzma

Summary:	Python bindings for the LZMA compression library
Name:		python-%{module}
Version:	0.5.3
Release:	%mkrel 1
License:	LGPLv2+
Group:		Development/Python
Url:		http://www.joachim-bauch.de/projects/python/pylzma
Source0:	http://www.joachim-bauch.de/projects/python/pylzma/releases/%{oname}-%{version}.tar.bz2
BuildRequires:	lzma-devel
BuildRequires:	python-devel
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


%changelog
* Sat Nov 27 2010 Funda Wang <fwang@mandriva.org> 0.5.2-3mdv2011.0
+ Revision: 601639
- rebuild for new liblzma

* Sun Oct 31 2010 Andrey Borzenkov <arvidjaar@mandriva.org> 0.5.2-2mdv2011.0
+ Revision: 590769
- rebuild for new python 2.7

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - new version

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.3.0-8mdv2010.0
+ Revision: 442306
- rebuild

* Sun Dec 28 2008 Funda Wang <fwang@mandriva.org> 0.3.0-7mdv2009.1
+ Revision: 320170
- rebuild for new python

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 0.3.0-6mdv2009.0
+ Revision: 259681
- rebuild

* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 0.3.0-5mdv2009.0
+ Revision: 247505
- rebuild

* Sun Feb 03 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.0-3mdv2008.1
+ Revision: 161881
- new license policy

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Sep 14 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.0-2mdv2008.0
+ Revision: 85744
- fix file list
- new name
- package docs
- python module name compiliant

* Sat Jun 16 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.0-1mdv2008.0
+ Revision: 40301
- Import pylzma

