Summary:	LGeneral game
Summary(pl):	Gra Linux General
Name:		lgeneral
Version:	1.1
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	ftp://ftp.sourceforge.net/pub/sourceforge/lgeneral/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Patch0:		%{name}-inst_dir.patch
Patch1:		%{name}-configure_fix.patch
URL:		http://lgames.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	SDL_mixer-devel >= 1.1.4
Requires:	%{name}-data >= 1.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
LGeneral is a turn-based strategy engine heavily inspired by Panzer
General. You play single scenarios or whole campaigns turn by turn
against a human player or the AI. Entrenchment, rugged defense,
defensive fire, surprise contacts, surrender, unit supply, weather
influence, reinforcements and other implementations contribute to the
tactical and strategic depth of the game.

%description -l pl
LGeneral jest turow± gr± strategiczn± zainspirowan± o Panzer General.
Mo¿na graæ scenariusze albo kampanie, przeciwko drugiemu graczowi albo
komputerowi. Gra posiada du¿o zaawansowanych opcji tj. wp³yw pogody na
warunki walki.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
rm -f missing
%{__aclocal}
%{__automake}
%{__autoconf}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/Games/Strategy

%{__make} DESTDIR=$RPM_BUILD_ROOT install

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Games/Strategy/%{name}.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
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
%{_applnkdir}/Games/Strategy/%{name}.desktop
