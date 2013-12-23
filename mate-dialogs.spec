#
# Conditional build:
%bcond_with	gtk3	# use GTK+ 3.x instead of 2.x
#
Summary:	Displays dialog boxes from shell scripts
Summary(pl.UTF-8):	Wyświetlanie okien dialogowych z poziomu skryptów powłoki
Name:		mate-dialogs
Version:	1.6.2
Release:	1
License:	LGPL v2+
Group:		X11/Applications
Source0:	http://pub.mate-desktop.org/releases/1.6/%{name}-%{version}.tar.xz
# Source0-md5:	c24922c2e88ee4741c33985786ca5fef
URL:		http://wiki.mate-desktop.org/mate-dialogs
%{!?with_gtk3:BuildRequires:	gtk+2-devel >= 2:2.18.0}
%{?with_gtk3:BuildRequires:	gtk+3-devel >= 3.0.0}
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libnotify-devel >= 0.7.0
BuildRequires:	mate-common
BuildRequires:	mate-doc-utils
BuildRequires:	pkgconfig
BuildRequires:	rarian-compat
BuildRequires:	rpmbuild(find_lang) >= 1.36
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
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
%configure \
	--enable-libnotify \
	--disable-silent-rules \
	%{?with_gtk3:--with-gtk=3.0}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# mate-dialogs gettext domain, matedialog mate help and omf files
%find_lang %{name} --with-omf --with-mate --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/matedialog
%{_mandir}/man1/matedialog.1*
%{_datadir}/matedialog
