%define	name			hso-rezero
%define oname			hso-udev
%define	version			0.1
%define release			%mkrel 2

Summary:		Tools for Option 3G cards
Name:			%{name}
Version:		%{version}
Release:		%{release}
# http://www.pharscape.org/component/option,com_forum/Itemid,68/page,viewtopic/t,425/
Source0:		%{oname}.tar.gz
Source2:		49_hso-udev.rules
URL:			http://www.pharscape.org/
Group:			System/Configuration/Hardware
BuildRoot:		%{_tmppath}/%{name}-buildroot
License:		GPL

%description
rezero is a utility to disable the ZeroCD (fake USB CD-Rom)
temporarily at run time for Option 3G cards.

%prep
%setup -q -c

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
