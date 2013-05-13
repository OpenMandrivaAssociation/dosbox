%define	name	dosbox
%define version 0.74
%define release  2
%define	Summary	A DOS emulator

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	%{Summary}

Source0:	http://prdownloads.sourceforge.net/dosbox/%{name}-%{version}.tar.bz2
Source11:	%{name}-16x16.png
Source12:	%{name}-32x32.png
Source13:	%{name}-48x48.png

Patch0:		dosbox-0.73-fix-str-fmt.patch
# patch for gcc-4.6. Thnx to Gentoo
Patch1:		dosbox-0.74-gcc46.patch

License:	GPL
Group:		Emulators
URL:		http://dosbox.sourceforge.net/
BuildRequires:	png-devel libSDL-devel libSDL_net-devel 
BuildRequires:  SDL_sound-devel = 1.0.3-11  
BuildRequires:  libalsa-devel zlib1-devel libx11-devel

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
%patch0 -p0
%patch1 -p0

%build
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall
rm -rf %{buildroot}%{_datadir}/doc/dosbox

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications

# Create appropriate .desktop file
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=DOSBox
Comment=A DOS emulator
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Emulator;
EOF


install -m644 %{SOURCE11} -D %{buildroot}%{_miconsdir}/%{name}.png
install -m644 %{SOURCE12} -D %{buildroot}%{_iconsdir}/%{name}.png
install -m644 %{SOURCE13} -D %{buildroot}%{_liconsdir}/%{name}.png

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


%changelog
* Fri Jun 1 2012 Anton Chernyshov <ach@rosalab.ru> 0.74-1rosalts2012.0
- Fixing BuildRequires
- Clean up spec
- Add patch from Gentoo to build with gcc-4.6 version
- initial build for ROSA Marathon 2012

* Sat Jul 10 2010 Zombie Ryushu <ryushu@mandriva.org> 0.74-1mdv2011.0
+ Revision: 550235
- string format fix
- Upgrade to 0.74
- Upgrade to 0.74

* Thu May 28 2009 Funda Wang <fwang@mandriva.org> 0.73-1mdv2010.0
+ Revision: 380341
- New version 0.73

* Sat Aug 23 2008 Emmanuel Andry <eandry@mandriva.org> 0.72-3mdv2009.0
+ Revision: 275268
- fix gcc43 build with P0 from fedora

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.72-1mdv2008.1
+ Revision: 136373
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'

* Mon Aug 27 2007 Funda Wang <fwang@mandriva.org> 0.72-1mdv2008.0
+ Revision: 72035
- New version 0.72

* Tue Jul 31 2007 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.71-1mdv2008.0
+ Revision: 57009
- new release: 0.71
- drop debian menu


* Sun Mar 04 2007 Per Øyvind Karlsen <pkarlsen@mandriva.com> 0.70-2mdv2007.0
+ Revision: 132307
- drop config file

* Sun Mar 04 2007 Emmanuel Andry <eandry@mandriva.org> 0.70-1mdv2007.1
+ Revision: 132116
- New version 0.70

* Sun Jan 14 2007 Emmanuel Andry <eandry@mandriva.org> 0.65-3mdv2007.1
+ Revision: 108652
- buildrequires mesaglu-devel
- fix buildrequires
- Import dosbox

* Wed Aug 02 2006 Götz Waschk <waschk@mandriva.org> 0.65-2mdv2007.0
- xdg menu

* Fri Mar 31 2006 Götz Waschk <waschk@mandriva.org> 0.65-1mdk
- New release 0.65
- use mkrel

* Thu Mar 10 2005 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.63-3mdk
- do not bzip2 icons in src.rpm
- convert changelog to utf8

* Tue Dec 07 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.63-2mdk
- from Miguel Barrio Orsikowsky <megamik@zarb.org> : 
	- changed BuildRequires
	- new configuration file
	- added SDL_sound-devel to BuildRequires
	- updated package description

* Fri Nov 19 2004 Götz Waschk <waschk@linux-mandrake.com> 0.63-1mdk
- New release 0.63

* Fri Oct 01 2004 Götz Waschk <waschk@linux-mandrake.com> 0.62-1mdk
- drop patch
- New release 0.62

* Fri Aug 20 2004 Götz Waschk <waschk@linux-mandrake.com> 0.61-3mdk
- rebuild for new menu

* Wed Jun 09 2004 Götz Waschk <waschk@linux-mandrake.com> 0.61-2mdk
- add source URL
- patch for new g++

