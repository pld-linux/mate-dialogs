#
# Conditional build:
%bcond_with	gtk3	# use GTK+ 3.x instead of 2.x
#
Summary:	Displays dialog boxes from shell scripts
Summary(pl.UTF-8):	Wyświetlanie okien dialogowych z poziomu skryptów powłoki
Name:		mate-dialogs
Version:	1.8.0
Release:	2
License:	LGPL v2+
Group:		X11/Applications
Source0:	http://pub.mate-desktop.org/releases/1.8/%{name}-%{version}.tar.xz
# Source0-md5:	c52cba1b3cb8c600e710e129a5118e84
URL:		http://wiki.mate-desktop.org/mate-dialogs
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
BuildRequires:	glib2-devel
%{!?with_gtk3:BuildRequires:	gtk+2-devel >= 2:2.18.0}
%{?with_gtk3:BuildRequires:	gtk+3-devel >= 3.0.0}
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libnotify-devel >= 0.7.0
BuildRequires:	mate-common
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(find_lang) >= 1.36
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xz
BuildRequires:	yelp-tools
%{!?with_gtk3:Requires:	gtk+2 >= 2:2.18.0}
%{?with_gtk3:Requires:	gtk+3 >= 3.0.0}
Requires:	libnotify >= 0.7.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Displays dialog boxes from shell scripts.

%description -l pl.UTF-8
Wyświetlanie okien dialogowych z poziomu skryptów powłoki.

%prep
%setup -q

%build
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-libnotify \
	--disable-silent-rules \
	%{?with_gtk3:--with-gtk=3.0}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# mate-dialogs gettext domain, matedialog mate help files
%find_lang %{name} --with-mate --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/matedialog
%{_mandir}/man1/matedialog.1*
%{_datadir}/matedialog
