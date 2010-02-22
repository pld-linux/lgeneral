Summary:	LGeneral game
Summary(pl.UTF-8):	Gra Linux General
Name:		lgeneral
Version:	1.2beta
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/lgeneral/%{name}-%{version}.tar.gz
# Source0-md5:	d89f6b574e0f182f04cd9b069225fc30
Source1:	%{name}.desktop
Patch0:		%{name}-inst_dir.patch
Patch1:		%{name}-configure_fix.patch
URL:		http://lgames.sourceforge.net/index.php?project=LGeneral
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	SDL_mixer-devel >= 1.1.4
Requires:	lgeneral-data >= 1.1
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
%setup -q
%patch0 -p1
#%patch1 -p1

%build
%{__aclocal}
%{__automake}
%{__autoconf}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop

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
