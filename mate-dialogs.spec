Summary:	Displays dialog boxes from shell scripts
Name:		mate-dialogs
Version:	1.5.0
Release:	1
Group:		X11/Applications
License:	LGPLv2+ and GPLv2+
URL:		http://mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/1.5/%{name}-%{version}.tar.xz
BuildRequires:	mate-common
BuildRequires:	mate-doc-utils
BuildRequires:	pkgconfig(gtk+)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	rarian-compat
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Displays dialog boxes from shell scripts.

%prep
%setup -q

%build
NOCONFIGURE=1 ./autogen.sh
%configure \
	--disable-static \
	--enable-libmatenotify

%{__make} \
	V=1

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING README
%attr(755,root,root) %{_bindir}/gdialog
%attr(755,root,root) %{_bindir}/matedialog
%{_mandir}/man1/*
%{_datadir}/mate/help/matedialog
%{_datadir}/omf/matedialog
%{_datadir}/matedialog