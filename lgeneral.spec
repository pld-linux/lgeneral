Summary:	Panzer General clone
Summary(pl.UTF-8):	Klon gry Panzer General
Name:		lgeneral
Version:	1.2.2
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games/Strategy
Source0:	http://downloads.sourceforge.net/lgeneral/%{name}-%{version}.tar.gz
# Source0-md5:	aa2a591a2f069a4dae530ff6920303cb
Source1:	http://downloads.sourceforge.net/lgeneral/pg-data.tar.gz
# Source1-md5:	40c4be23f60d1dc732aabe13b58fc5e3
Source2:	%{name}.desktop
URL:		http://lgames.sourceforge.net/index.php?project=LGeneral
BuildRequires:	SDL_mixer-devel >= 1.1.4
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-tools
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
LGeneral jest turową grą strategiczną zainspirowaną przez Panzer
General. Gracz rozgrywa scenariusze lub całe kampanie przeciwko
drugiemu graczowi lub komputerowi. Gra posiada dużo zaawansowanych
opcji jak na przykład wpływ pogody na warunki walki.

%prep
%setup -q -a 1
%{__sed} -i 's@games/@@' configure.in
#Maybe somebody know better way?
cp %{_datadir}/gettext/config.rpath .

%build
%configure

%{__make} -j1 \
	ACLOCAL="%{__aclocal}" \
	AUTOMAKE="%{__automake}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop
cp -r pg-data $RPM_BUILD_ROOT%{_datadir}/%{name}
mv $RPM_BUILD_ROOT%{_iconsdir}/{lgeneral48.png,lgeneral.png}

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
CD, you can use the abandonware pg-data package
by run the following command as root user:

	lgc-pg -s /usr/share/lgeneral/pg-data -d /usr/share/lgeneral

EOF
fi

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README.lg* TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_mandir}/man[16]/*.*
%{_iconsdir}/%{name}.png
