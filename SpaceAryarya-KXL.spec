Summary:	Space Aryarya, a video-oriented game
Summary(pl):	Space Aryarya - gra wideo
Name:		SpaceAryarya-KXL
Version:	1.0.2
Release:	2
License:	GPL
Group:		X11/Applications/Games
Source0:	http://kxl.hn.org/download/%{name}-%{version}.tar.gz
# Source0-md5:	0c3666630eed179d9d3c0182b6358a6f
Patch0:		%{name}-scorepath.patch
URL:		http://kxl.hn.org/
BuildRequires:	KXL-devel >= 1.1.1
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	KXL >= 1.1.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
2D/3D scroll shooting game.

%description -l pl
Przewijana strzelanina 2D/3D.

%prep
%setup -q
%patch -p1

%build
cp -f /usr/share/automake/config.sub .
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(2755,root,games) %{_bindir}/spacearyarya
%dir %{_datadir}/SpaceAryarya
%dir %{_datadir}/SpaceAryarya/data
%{_datadir}/SpaceAryarya/bmp
%{_datadir}/SpaceAryarya/wav
%{_datadir}/SpaceAryarya/data/*.dat
%attr(664,root,games) %config(noreplace) %verify(not size mtime md5) /var/games/SpaceAryarya.score
