Summary:	Displays dialog boxes from shell scripts
Name:		mate-dialogs
Version:	1.5.0
Release:	1
License:	LGPL v2+ and GPL v2+
Group:		X11/Applications
Source0:	http://pub.mate-desktop.org/releases/1.5/%{name}-%{version}.tar.xz
# Source0-md5:	3c38db321f01ccf46fa7a48917e1a306
URL:		http://wiki.mate-desktop.org/mate-dialogs
BuildRequires:	gtk+-devel
BuildRequires:	gtk+2-devel
BuildRequires:	libmatenotify-devel >= 1.1.0
BuildRequires:	mate-common
BuildRequires:	mate-doc-utils
BuildRequires:	rarian-compat
BuildRequires:	rpmbuild(find_lang) >= 1.36
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
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

%find_lang %{name} --with-omf --with-mate --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING README
%attr(755,root,root) %{_bindir}/gdialog
%attr(755,root,root) %{_bindir}/matedialog
%{_mandir}/man1/matedialog.1*
%{_datadir}/matedialog
