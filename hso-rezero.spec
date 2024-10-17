%define	name			hso-rezero
%define oname			hso-udev
%define	version			0.1
%define release			9
%define debug_package          %{nil}

Summary:		Tools for Option 3G cards
Name:			%{name}
Version:		%{version}
Release:		%{release}
# http://www.pharscape.org/component/option,com_forum/Itemid,68/page,viewtopic/t,425/
Source0:		%{oname}.tar.gz
Source2:		49_hso-udev.rules
URL:			https://www.pharscape.org/
Group:			System/Configuration/Hardware
BuildRoot:		%{_tmppath}/%{name}-buildroot
License:		GPL

%description
rezero is a utility to disable the ZeroCD (fake USB CD-Rom)
temporarily at run time for Option 3G cards.

%prep
%setup -q -c
make clean

%build
%make 

%install
rm -rf %{buildroot}
%makeinstall_std
mkdir -p %{buildroot}/%_sbindir
mkdir -p %{buildroot}/%_sysconfdir/hal/fdi/policy/
mkdir -p %{buildroot}/%_sysconfdir/udev/rules.d/
rm -f %buildroot/%_sysconfdir/udev/rules.d/*.rules
install -m 644 %{SOURCE2} %buildroot/%_sysconfdir/udev/rules.d/

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root,0755)
%{_sbindir}/*
%{_sysconfdir}/udev/rules.d/*.rules


%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1-8mdv2011.0
+ Revision: 611101
- rebuild

* Wed Feb 03 2010 Frederic Crozat <fcrozat@mandriva.com> 0.1-7mdv2010.1
+ Revision: 500301
- Really fix obsolete syntax in udev rules

* Wed Feb 03 2010 Frederic Crozat <fcrozat@mandriva.com> 0.1-6mdv2010.1
+ Revision: 500298
- Fix udev rules

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Wed Feb 04 2009 Olivier Blin <oblin@mandriva.com> 0.1-4mdv2009.1
+ Revision: 337515
- add support for Huawei K3175 (aka E620) from Fabrice Gamberini (Dexxon)

* Wed Jan 28 2009 Olivier Blin <oblin@mandriva.com> 0.1-3mdv2009.1
+ Revision: 334897
- rebuild build the binary, do not reuse x86 one from tarball (useful for MIPS...)

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 0.1-2mdv2009.0
+ Revision: 267098
- rebuild early 2009.0 package (before pixel changes)

* Fri May 23 2008 Olivier Blin <oblin@mandriva.com> 0.1-1mdv2009.0
+ Revision: 210675
- use makeinstall_std
- use System/Configuration/Hardware as group
- update summary and description
- remove hardcoded prefix
- remove hardcoded packager tag
- do not own udev dir
- remove upstream udev rule
- use upstream tarball
- adapt to new naming and versionning
- initial hso-rezero package (from vguardiola)
- create hso-rezero

