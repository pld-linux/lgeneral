%define _bver	13
%define	_beta	beta-%{_bver}
Summary:	LGeneral game
Summary(pl.UTF-8):	Gra Linux General
Name:		lgeneral
Version:	1.2
Release:	0.beta%{_bver}.1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/lgeneral/%{name}-%{version}%{_beta}.tar.gz
# Source0-md5:	ac8d4ec71a2e263d38a650a158e25da5
Source1:	http://dl.sourceforge.net/lgeneral/pg-data.tar.gz
# Source1-md5:	40c4be23f60d1dc732aabe13b58fc5e3
Source2:	%{name}.desktop
URL:		http://lgames.sourceforge.net/
BuildRequires:  SDL_mixer-devel >= 1.1.4
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LGeneral is a turn-based strategy engine heavily inspired by Panzer
General. You play single scenarios or whole campaigns turn by turn
against a human player or the AI. Entrenchment, rugged defense,
defensive fire, surprise contacts, surrender, unit supply, weather
influence, reinforcements and other implementations contribute to the
tactical and strategic depth of the game.

%description -l pl.UTF-8
LGeneral jest turową grą strategiczną zainspirowaną o Panzer General.
Można grać scenariusze albo kampanie, przeciwko drugiemu graczowi albo
komputerowi. Gra posiada dużo zaawansowanych opcji tj. wpływ pogody na
warunki walki.

%prep
%setup -q -n %{name}-%{version}%{_beta}
%{__sed} -i 's@$datadir/games/lgeneral@$datadir/lgeneral@' configure.in

%build
%configure

cp /usr/share/gettext/config.rpath .
%{__make} \
	ACLOCAL="%{__aclocal}" \
	AUTOMAKE="automake -a -c -f"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README.lgeneral TODO
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/ai_modules
%dir %{_datadir}/%{name}/campaigns
%dir %{_datadir}/%{name}/gfx
%dir %{_datadir}/%{name}/gfx/flags
%dir %{_datadir}/%{name}/gfx/terrain
%dir %{_datadir}/%{name}/gfx/units
%{_datadir}/%{name}/gfx/*.bmp
%dir %{_datadir}/%{name}/maps
%dir %{_datadir}/%{name}/music
%dir %{_datadir}/%{name}/nations
%dir %{_datadir}/%{name}/scenarios
%dir %{_datadir}/%{name}/sounds
%dir %{_datadir}/%{name}/themes
%{_datadir}/%{name}/themes/*
%dir %{_datadir}/%{name}/units
%{_desktopdir}/%{name}.desktop
