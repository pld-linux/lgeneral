Summary:	LGeneral game
Summary(pl):	Gra Linux General
Name:		LGeneral
Version:	1.1
Release:	1
License:	GPL
Group:		X11/Games
Source0:	http://ftp1.sourceforge.net/lgeneral/%{name}-%{version}.tar.gz
Source1: %{name}.desktop
URL:		http://lgames.sourceforge.net/
BuildRequires:	SDL-devel >= 1.1.4
BuildRequires:	SDL_mixer >= 1.1.4
#BuildRequires:	lgeneral-data >= 1.1.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_applnkdir		/usr/X11R6/share/applnk

%description
LGeneral is a turn-based strategy engine heavily inspired by Panzer General. You

play single scenarios or whole campaigns turn by turn against a human player or
the AI. Entrenchment, rugged defense, defensive fire, surprise contacts,
surrender, unit supply, weather influence, reinforcements and other
implementations contribute to the tactical and strategic depth of the game.

%description -l pl
LGeneral jest turow± gr± strategiczn± zainspirowan± o Panzer General. Mo¿na graæ
scenariusze albo kampanie, przeciwko drugiemu graczowi albo komputerowi. Gra
posiada du¿o zaawansowanych opcji tj. wp³yw pogody na warunki walki.

%prep
%setup -q

%build

%configure2_13

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/X11R6/share/applnk/Games
install %{SOURCE1} $RPM_BUILD_ROOT/usr/X11R6/share/applnk/Games

%{__make} DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/games/lgeneral/themes/default/*.bmp
%{_datadir}/games/lgeneral/gfx/*.bmp
%{_datadir}/games/lgeneral/themes/default/*.wav
%{_applnkdir}/Games/LGeneral.desktop
