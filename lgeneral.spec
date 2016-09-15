Summary:	Panzer General clone
Summary(pl.UTF-8):	Klon gry Panzer General
Name:		lgeneral
Version:	1.2.2
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games/Strategy
Source0:	http://downloads.sourceforge.net/lgeneral/%{name}-%{version}.tar.gz
# Source0-md5:	aa2a591a2f069a4dae530ff6920303cb
Source1:	%{name}.desktop
Patch0:		%{name}-hash.patch
Patch1:		%{name}-format.patch
URL:		http://lgames.sourceforge.net/LGeneral
BuildRequires:	SDL-devel >= 1.1.4
BuildRequires:	SDL_mixer-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-tools
BuildRequires:	sed >= 4.0
Requires:	SDL >= 1.1.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LGeneral is a turn-based strategy engine heavily inspired by Panzer
General. You play single scenarios or whole campaigns turn by turn
against a human player or the AI. Entrenchment, rugged defense,
defensive fire, surprise contacts, surrender, unit supply, weather
influence, reinforcements and other implementations contribute to the
tactical and strategic depth of the game.

%description -l pl.UTF-8
LGeneral jest turową grą strategiczną zainspirowaną przez Panzer
General. Gracz rozgrywa scenariusze lub całe kampanie przeciwko
drugiemu graczowi lub komputerowi. Gra posiada dużo zaawansowanych
opcji jak na przykład wpływ pogody na warunki walki.

%prep
%setup -q
#patch0 -p1 # if using updated intl/
%patch1 -p1

%{__sed} -i 's@games/@@' configure.in

%build
# cannot use gettextize (po/ is hacked), so just
cp -f %{_datadir}/gettext/config.rpath .
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop
%{__mv} $RPM_BUILD_ROOT%{_iconsdir}/{lgeneral48.png,lgeneral.png}

# lgeneral,pg domains
%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ "$1" = 1 ]; then
%banner %{name} -e <<EOF
NOTE:
If you have the orginal Panzer General CD then mount it
(e.g., to /mnt/cdrom) and run the following command as root user:

	lgc-pg -s /mnt/cdrom/DAT -d /usr/share/lgeneral

If you do not have the orginal Panzer General
CD, you can use the abandonware lgeneral-data-pg package
by (after installing it) running the following command as root user:

	lgc-pg -s /usr/share/lgeneral/pg-data -d /usr/share/lgeneral

EOF
fi

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog PanzerGeneral-Guru.txt README.{lgc-pg,lgeneral} TODO
%attr(755,root,root) %{_bindir}/lgc-pg
%attr(755,root,root) %{_bindir}/lged
%attr(755,root,root) %{_bindir}/lgeneral
%attr(755,root,root) %{_bindir}/ltrextract
%attr(755,root,root) %{_bindir}/shptool
%dir %{_datadir}/lgeneral
%dir %{_datadir}/lgeneral/ai_modules
%dir %{_datadir}/lgeneral/campaigns
%{_datadir}/lgeneral/campaigns/PG
%{_datadir}/lgeneral/convdata
%{_datadir}/lgeneral/gfx
%dir %{_datadir}/lgeneral/maps
%dir %{_datadir}/lgeneral/music
%dir %{_datadir}/lgeneral/nations
%dir %{_datadir}/lgeneral/scenarios
%dir %{_datadir}/lgeneral/sounds
%dir %{_datadir}/lgeneral/terrain
%dir %{_datadir}/lgeneral/themes
%{_datadir}/lgeneral/themes/default
%dir %{_datadir}/lgeneral/units
%{_desktopdir}/%{name}.desktop
%{_mandir}/man1/lgc-pg.1*
%{_mandir}/man6/lgeneral.6*
%{_iconsdir}/%{name}.png
