Summary:	A DOS emulator
Name:		dosbox
Version:	0.74
Release:	4
License:	GPLv2+
Group:		Emulators
Url:		http://dosbox.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/dosbox/%{name}-%{version}.tar.bz2
Source11:	%{name}-16x16.png
Source12:	%{name}-32x32.png
Source13:	%{name}-48x48.png
Patch0:		dosbox-0.73-fix-str-fmt.patch
# patch for gcc-4.6. Thnx to Gentoo
Patch1:		dosbox-0.74-gcc46.patch
BuildRequires:	SDL_sound-devel
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(SDL_net)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(zlib)

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

%files
%doc AUTHORS ChangeLog NEWS README THANKS
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_mandir}/*/*
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p0
%patch1 -p0

%build
%configure2_5x
%make

%install
%makeinstall_std

rm -rf %{buildroot}%{_datadir}/doc/dosbox

mkdir -p %{buildroot}%{_datadir}/applications

# Create appropriate .desktop file
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=DOSBox
Comment=A DOS emulator
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Utility;Emulator;
EOF

install -m644 %{SOURCE11} -D %{buildroot}%{_miconsdir}/%{name}.png
install -m644 %{SOURCE12} -D %{buildroot}%{_iconsdir}/%{name}.png
install -m644 %{SOURCE13} -D %{buildroot}%{_liconsdir}/%{name}.png

