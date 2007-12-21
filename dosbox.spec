%define	name	dosbox
%define version 0.72
%define release %mkrel 1
%define	Summary	A DOS emulator

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	%{Summary}
Source0:	http://prdownloads.sourceforge.net/dosbox/%{name}-%{version}.tar.gz
#Source2:	%{name}.conf.bz2
Source11:	%{name}-16x16.png
Source12:	%{name}-32x32.png
Source13:	%{name}-48x48.png
License:	GPL
Group:		Emulators
URL:		http://dosbox.sourceforge.net/
BuildRequires:	png-devel SDL-devel SDL_net-devel SDL_sound-devel mesaglu-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
DOSBox is a DOS-emulator that uses the SDL-library which makes
DOSBox very easy to port to different platforms. DOSBox has
already been ported to many different platforms, such as
Windows, BeOS, Linux, MacOS X...

DOSBox also emulates CPU:286/386 realmode/protected mode,
Directory FileSystem/XMS/EMS, Tandy/Hercules/CGA/EGA/VGA/VESA
graphics, a SoundBlaster/Gravis Ultra Sound card for excellent
sound compatibility with older games...

You can "re-live" the good old days with the help of DOSBox,
it can run plenty of the old classics that don't run on your
new computer!

%prep
%setup -q

%build
%configure2_5x	--enable-core-inline
%make

%install
rm -rf %{buildroot}
%makeinstall
rm -rf %{buildroot}%{_datadir}/doc/dosbox

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=DOSBox
Comment=A DOS emulator
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=X-MandrivaLinux-MoreApplications-Emulators;Emulator;
EOF


install -m644 %{SOURCE11} -D %{buildroot}%{_miconsdir}/%{name}.png
install -m644 %{SOURCE12} -D %{buildroot}%{_iconsdir}/%{name}.png
install -m644 %{SOURCE13} -D %{buildroot}%{_liconsdir}/%{name}.png

%post
%update_menus

%postun
%clean_menus

%clean
rm -rf %{buildroot}

%files
%defattr(755,root,root,755)
%{_bindir}/%{name}
%defattr(644,root,root,755)
%{_mandir}/*/*
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_datadir}/applications/*.desktop
%doc AUTHORS ChangeLog NEWS README THANKS
