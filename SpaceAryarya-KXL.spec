#
# TODO: move score file(s) to /var/games
#
Summary:	Space Aryarya, a video-oriented game
Summary(pl):	Space Aryarya - gra wideo
Name:		SpaceAryarya-KXL
Version:	1.0.2
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source:		http://kxl.hn.org/download/%{name}-%{version}.tar.gz
URL:		http://kxl.hn.org/
BuildRequires:	KXL-devel >= 1.1.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
2D/3D scroll shooting game.

%description -l pl
Przewijana strzelanina 2D/3D.

%prep
%setup -q

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/spacearyarya
%dir %{_datadir}/SpaceAryarya
%dir %{_datadir}/SpaceAryarya/data
%{_datadir}/SpaceAryarya/bmp
%{_datadir}/SpaceAryarya/wav
%{_datadir}/SpaceAryarya/data/*.dat
# MOVE TO /var/games!!!
%config(noreplace) %{_datadir}/SpaceAryarya/data/.score
