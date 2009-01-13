%define         gstreamer       gstreamer
%define         majorminor      0.10

%define         _gst            0.10.21

Name: 		%{gstreamer}-plugins-base
Version: 	0.10.21
Release:  	4%{?dist}	
Summary: 	GStreamer streaming media framework base plug-ins

Group: 		Applications/Multimedia
License: 	LGPLv2+
URL:		http://gstreamer.freedesktop.org/
Source:		http://gstreamer.freedesktop.org/src/gst-plugins-base/gst-plugins-base-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Patch0:		gstpb-0.10.15-cd-speed.patch
# http://bugzilla.gnome.org/show_bug.cgi?id=556986
Patch1:		gstpb-pulse-hang-bz556986.patch

Requires:       %{gstreamer} >= %{_gst}
Requires:	liboil >= 0.3.12-9
BuildRequires: 	%{gstreamer}-devel >= %{_gst}

BuildRequires:  gettext
BuildRequires:  gcc-c++

BuildRequires:  libogg-devel >= 1.0
BuildRequires:  libvorbis-devel >= 1.0
BuildRequires:  libtheora-devel >= 1.0
BuildRequires:  liboil-devel >= 0.3.6
BuildRequires:  alsa-lib-devel
BuildRequires:  pango-devel
BuildRequires:  libXv-devel
BuildRequires:  cdparanoia-devel
BuildRequires:  libvisual-devel
BuildRequires:  gtk2-devel
BuildRequires:  pkgconfig
Obsoletes:	gstreamer-plugins

# documentation
BuildRequires:  gtk-doc >= 1.3
BuildRequires:  PyXML

%description
GStreamer is a streaming media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new
plug-ins.

This package contains a set of well-maintained base plug-ins.

%prep
%setup -q -n gst-plugins-base-%{version}
%patch0 -p1 -b .cd-speed
%patch1 -p0 -b .pulse-hang

%build
%configure \
  --with-package-name='Fedora gstreamer-plugins-base package' \
  --with-package-origin='http://download.fedora.redhat.com/fedora' \
  --enable-gtk-doc \
  --enable-experimental \
  --disable-static

make %{?_smp_mflags} ERROR_CFLAGS=""

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall

# Clean out files that should not be part of the rpm.
rm -f $RPM_BUILD_ROOT%{_libdir}/gstreamer-%{majorminor}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/gstreamer-%{majorminor}/*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{_bindir}/gst-visualise*
rm -f $RPM_BUILD_ROOT%{_mandir}/man1/gst-visualise*

%find_lang gst-plugins-base-%{majorminor}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f gst-plugins-base-%{majorminor}.lang
%defattr(-, root, root)
%doc AUTHORS COPYING README REQUIREMENTS

# libraries
%{_libdir}/libgstinterfaces-%{majorminor}.so.*
%{_libdir}/libgstaudio-%{majorminor}.so.*
%{_libdir}/libgstcdda-%{majorminor}.so.*
%{_libdir}/libgstfft-%{majorminor}.so.*
%{_libdir}/libgstriff-%{majorminor}.so.*
%{_libdir}/libgsttag-%{majorminor}.so.*
%{_libdir}/libgstnetbuffer-%{majorminor}.so.*
%{_libdir}/libgstrtp-%{majorminor}.so.*
%{_libdir}/libgstvideo-%{majorminor}.so.*
%{_libdir}/libgstpbutils-%{majorminor}.so.*
%{_libdir}/libgstrtsp-%{majorminor}.so.*
%{_libdir}/libgstsdp-%{majorminor}.so.*

# base plugins without external dependencies
%{_libdir}/gstreamer-%{majorminor}/libgstadder.so
%{_libdir}/gstreamer-%{majorminor}/libgstaudioconvert.so
%{_libdir}/gstreamer-%{majorminor}/libgstaudiotestsrc.so
%{_libdir}/gstreamer-%{majorminor}/libgstffmpegcolorspace.so
%{_libdir}/gstreamer-%{majorminor}/libgstdecodebin.so
%{_libdir}/gstreamer-%{majorminor}/libgstdecodebin2.so
%{_libdir}/gstreamer-%{majorminor}/libgstplaybin.so
%{_libdir}/gstreamer-%{majorminor}/libgsttypefindfunctions.so
%{_libdir}/gstreamer-%{majorminor}/libgstvideotestsrc.so
%{_libdir}/gstreamer-%{majorminor}/libgstaudiorate.so
%{_libdir}/gstreamer-%{majorminor}/libgstsubparse.so
%{_libdir}/gstreamer-%{majorminor}/libgstvolume.so
%{_libdir}/gstreamer-%{majorminor}/libgstvideorate.so
%{_libdir}/gstreamer-%{majorminor}/libgstvideoscale.so
%{_libdir}/gstreamer-%{majorminor}/libgsttcp.so
%{_libdir}/gstreamer-%{majorminor}/libgstvideo4linux.so
%{_libdir}/gstreamer-%{majorminor}/libgstaudioresample.so
%{_libdir}/gstreamer-%{majorminor}/libgstgdp.so
%{_libdir}/gstreamer-%{majorminor}/libgstqueue2.so
%{_libdir}/gstreamer-%{majorminor}/libgstgio.so

# base plugins with dependencies
%{_libdir}/gstreamer-%{majorminor}/libgstalsa.so
%{_libdir}/gstreamer-%{majorminor}/libgstcdparanoia.so
%{_libdir}/gstreamer-%{majorminor}/libgstlibvisual.so
%{_libdir}/gstreamer-%{majorminor}/libgstogg.so
%{_libdir}/gstreamer-%{majorminor}/libgstpango.so
%{_libdir}/gstreamer-%{majorminor}/libgsttheora.so
%{_libdir}/gstreamer-%{majorminor}/libgstvorbis.so
%{_libdir}/gstreamer-%{majorminor}/libgstximagesink.so
%{_libdir}/gstreamer-%{majorminor}/libgstxvimagesink.so

%package devel
Summary: 	GStreamer Base Plugins Development files
Group: 		Development/Libraries
Requires: 	%{gstreamer}-plugins-base = %{version}
Obsoletes:	gstreamer-plugins-devel

%description devel
GStreamer Base Plugins library development and header files.

%files devel
%defattr(-, root, root)
# plugin helper library headers
%dir %{_includedir}/gstreamer-%{majorminor}/gst/audio
%{_includedir}/gstreamer-%{majorminor}/gst/audio/audio.h
%{_includedir}/gstreamer-%{majorminor}/gst/audio/gstaudioclock.h
%{_includedir}/gstreamer-%{majorminor}/gst/audio/gstaudiofilter.h
%{_includedir}/gstreamer-%{majorminor}/gst/audio/gstaudiosink.h
%{_includedir}/gstreamer-%{majorminor}/gst/audio/gstaudiosrc.h
%{_includedir}/gstreamer-%{majorminor}/gst/audio/gstbaseaudiosink.h
%{_includedir}/gstreamer-%{majorminor}/gst/audio/gstbaseaudiosrc.h
%{_includedir}/gstreamer-%{majorminor}/gst/audio/gstringbuffer.h
%{_includedir}/gstreamer-%{majorminor}/gst/audio/mixerutils.h
%{_includedir}/gstreamer-%{majorminor}/gst/audio/multichannel-enumtypes.h
%{_includedir}/gstreamer-%{majorminor}/gst/audio/multichannel.h
%dir %{_includedir}/gstreamer-%{majorminor}/gst/cdda
%{_includedir}/gstreamer-%{majorminor}/gst/cdda/gstcddabasesrc.h
%dir %{_includedir}/gstreamer-%{majorminor}/gst/floatcast
%{_includedir}/gstreamer-%{majorminor}/gst/floatcast/floatcast.h
%dir %{_includedir}/gstreamer-%{majorminor}/gst/fft
%{_includedir}/gstreamer-%{majorminor}/gst/fft/gstfft*.h
%dir %{_includedir}/gstreamer-%{majorminor}/gst/interfaces
%{_includedir}/gstreamer-%{majorminor}/gst/interfaces/colorbalance.h
%{_includedir}/gstreamer-%{majorminor}/gst/interfaces/colorbalancechannel.h
%{_includedir}/gstreamer-%{majorminor}/gst/interfaces/interfaces-enumtypes.h
%{_includedir}/gstreamer-%{majorminor}/gst/interfaces/mixer.h
%{_includedir}/gstreamer-%{majorminor}/gst/interfaces/mixeroptions.h
%{_includedir}/gstreamer-%{majorminor}/gst/interfaces/mixertrack.h
%{_includedir}/gstreamer-%{majorminor}/gst/interfaces/navigation.h
%{_includedir}/gstreamer-%{majorminor}/gst/interfaces/propertyprobe.h
%{_includedir}/gstreamer-%{majorminor}/gst/interfaces/tuner.h
%{_includedir}/gstreamer-%{majorminor}/gst/interfaces/tunerchannel.h
%{_includedir}/gstreamer-%{majorminor}/gst/interfaces/tunernorm.h
%{_includedir}/gstreamer-%{majorminor}/gst/interfaces/videoorientation.h
%{_includedir}/gstreamer-%{majorminor}/gst/interfaces/xoverlay.h
%dir %{_includedir}/gstreamer-%{majorminor}/gst/netbuffer
%{_includedir}/gstreamer-%{majorminor}/gst/netbuffer/gstnetbuffer.h
%dir %{_includedir}/gstreamer-%{majorminor}/gst/pbutils
%{_includedir}/gstreamer-%{majorminor}/gst/pbutils/descriptions.h
%{_includedir}/gstreamer-%{majorminor}/gst/pbutils/install-plugins.h
%{_includedir}/gstreamer-%{majorminor}/gst/pbutils/missing-plugins.h
%{_includedir}/gstreamer-%{majorminor}/gst/pbutils/pbutils.h
%{_includedir}/gstreamer-%{majorminor}/gst/pbutils/pbutils-enumtypes.h
%dir %{_includedir}/gstreamer-%{majorminor}/gst/riff
%{_includedir}/gstreamer-%{majorminor}/gst/riff/riff-ids.h
%{_includedir}/gstreamer-%{majorminor}/gst/riff/riff-media.h
%{_includedir}/gstreamer-%{majorminor}/gst/riff/riff-read.h
%dir %{_includedir}/gstreamer-%{majorminor}/gst/rtp
%{_includedir}/gstreamer-%{majorminor}/gst/rtp/gstbasertpaudiopayload.h
%{_includedir}/gstreamer-%{majorminor}/gst/rtp/gstbasertpdepayload.h
%{_includedir}/gstreamer-%{majorminor}/gst/rtp/gstbasertppayload.h
%{_includedir}/gstreamer-%{majorminor}/gst/rtp/gstrtcpbuffer.h
%{_includedir}/gstreamer-%{majorminor}/gst/rtp/gstrtpbuffer.h
%{_includedir}/gstreamer-%{majorminor}/gst/rtp/gstrtppayloads.h
%dir %{_includedir}/gstreamer-%{majorminor}/gst/rtsp
%{_includedir}/gstreamer-%{majorminor}/gst/rtsp/gstrtsp-enumtypes.h
%{_includedir}/gstreamer-%{majorminor}/gst/rtsp/gstrtspbase64.h
%{_includedir}/gstreamer-%{majorminor}/gst/rtsp/gstrtspconnection.h
%{_includedir}/gstreamer-%{majorminor}/gst/rtsp/gstrtspdefs.h
%{_includedir}/gstreamer-%{majorminor}/gst/rtsp/gstrtspextension.h
%{_includedir}/gstreamer-%{majorminor}/gst/rtsp/gstrtspmessage.h
%{_includedir}/gstreamer-%{majorminor}/gst/rtsp/gstrtsprange.h
%{_includedir}/gstreamer-%{majorminor}/gst/rtsp/gstrtsptransport.h
%{_includedir}/gstreamer-%{majorminor}/gst/rtsp/gstrtspurl.h
%dir %{_includedir}/gstreamer-%{majorminor}/gst/sdp/
%{_includedir}/gstreamer-%{majorminor}/gst/sdp/gstsdp.h
%{_includedir}/gstreamer-%{majorminor}/gst/sdp/gstsdpmessage.h
%dir %{_includedir}/gstreamer-%{majorminor}/gst/tag
%{_includedir}/gstreamer-%{majorminor}/gst/tag/tag.h
%{_includedir}/gstreamer-%{majorminor}/gst/tag/gsttagdemux.h
%dir %{_includedir}/gstreamer-%{majorminor}/gst/video
%{_includedir}/gstreamer-%{majorminor}/gst/video/gstvideofilter.h
%{_includedir}/gstreamer-%{majorminor}/gst/video/gstvideosink.h
%{_includedir}/gstreamer-%{majorminor}/gst/video/video.h

%{_libdir}/libgstaudio-%{majorminor}.so
%{_libdir}/libgstinterfaces-%{majorminor}.so
%{_libdir}/libgstnetbuffer-%{majorminor}.so
%{_libdir}/libgstriff-%{majorminor}.so
%{_libdir}/libgstrtp-%{majorminor}.so
%{_libdir}/libgsttag-%{majorminor}.so
%{_libdir}/libgstvideo-%{majorminor}.so
%{_libdir}/libgstcdda-%{majorminor}.so
%{_libdir}/libgstpbutils-%{majorminor}.so
%{_libdir}/libgstrtsp-%{majorminor}.so
%{_libdir}/libgstsdp-%{majorminor}.so
%{_libdir}/libgstfft-%{majorminor}.so

# pkg-config files
%{_libdir}/pkgconfig/*.pc

# gtk-doc documentation
%doc %{_datadir}/gtk-doc/html/gst-plugins-base-libs-%{majorminor}
%doc %{_datadir}/gtk-doc/html/gst-plugins-base-plugins-%{majorminor}

%changelog
* Tue Jan 13 2009 - Bastien Nocera <bnocera@redhat.com> - 0.10.2-4
- Avoid deadlocks when PulseAudio disappears

* Thu Jan 1 2009 - Rex Dieter <rdieter@fedoraproject.org> - 0.10.2-3
- rebuild for pkgconfig deps (#478577)

* Fri Oct 03 2008 - Bastien Nocera <bnocera@redhat.com> - 0.10.21-2
- Update the gstreamer requirement
- Add a gtk2-devel BR, so that the test-colorkey program will be built

* Fri Oct 03 2008 - Bastien Nocera <bnocera@redhat.com> - 0.10.21-1
- Update to 0.10.21

* Wed Sep 24 2008 Jeremy Katz <katzj@redhat.com> - 0.10.20-6
- gst-visualize is just a test program that we don't really need to include 
  and having it means that perl gets pulled into small images (#462620)

* Fri Sep 12 2008 - Bastien Nocera <bnocera@redhat.com> - 0.10.20-4
- Another rebuild

* Thu Sep 11 2008 - Bastien Nocera <bnocera@redhat.com> - 0.10.20-3
- Rebuild for new RPM provides

* Sat Aug 23 2008 - Bastien Nocera <bnocera@redhat.com> - 0.10.20-2
- Fix useless codeina popup when playing recent ogg files (#458404)

* Wed Jun 18 2008 - Bastien Nocera <bnocera@redhat.com> - 0.10.20-1
- Update to 0.10.20

* Wed Jun 11 2008 - Bastien Nocera <bnocera@redhat.com> - 0.10.19-6
- Add patch full of gio fixes

* Mon Jun 02 2008 - Bastien Nocera <bnocera@redhat.com> - 0.10.19-5
- Let the package build its own documentation

* Sat May 24 2008 - Bastien Nocera <bnocera@redhat.com> - 0.10.19-4
- Remove the gnome-vfs plugin, and see what breaks

* Wed May 21 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.10.19-3
- fix license tag

* Fri Apr 18 2008 - Bastien Nocera <bnocera@redhat.com> - 0.10.19-2
- Add patch to avoid sync problems in the ALSA sink when a specific
  track has both playback and record flags

* Fri Apr 04 2008 - Bastien Nocera <bnocera@redhat.com> - 0.10.19-1
- Update to 0.10.19

* Tue Mar 25 2008 - Bastien Nocera <bnocera@redhat.com> - 0.10.18-1
- Update to 0.10.18
- Re-enable the libvisual plugins

* Sun Mar 09 2008 - Bastien Nocera <bnocera@redhat.com> - 0.10.17.2-4
- Disable libvisual for now (#435771)

* Tue Mar 04 2008 Adam Jackson <ajax@redhat.com> 0.10.17.2-3
- gstpb-0.10.15-cd-speed.patch: Set default CD read speed to something
  sensible. (#431178)
- s/Fedora Core/Fedora/
- Don't even bother building static libs.

* Tue Mar 04 2008 - Bastien Nocera <bnocera@redhat.com> - 0.10.17.2-2
- Enable the GIO plugin

* Tue Mar 04 2008 - Bastien Nocera <bnocera@redhat.com> - 0.10.17.2-1
- Update to 0.10.17.2 pre-release

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.10.17-2
- Autorebuild for GCC 4.3

* Wed Jan 30 2008 - Bastien Nocera <bnocera@redhat.com> - 0.10.17-1
- Update to 0.10.17

* Tue Jan 29 2008 - Bastien Nocera <bnocera@redhat.com> - 0.10.16-1
- Update to 0.10.16

* Sun Jan 20 2008  Matthias Clasen  <mclasen@redhat.com> - 0.10.15-3
- Fix upgrade path

* Mon Jan 07 2008 - Bastien Nocera <bnocera@redhat.com> - 0.10.15-2
- Add upstream patch to fix default track selection on Thinkpads
  (#344911)

* Sat Nov 17 2007 - Bastien Nocera <bnocera@redhat.com> - 0.10.15-1
- Update to 0.10.15

* Thu Oct 18 2007 - Bastien Nocera <bnocera@redhat.com> - 0.10.14-6
- Add patch to fix playback of short Ogg Vorbis files (#328851)

* Wed Aug 29 2007 - Bastien Nocera <bnocera@redhat.com> - 0.10.14-5
- Add patch to avoid critical warning when getting information about
  missing codecs
- Up liboil requirement

* Tue Aug 28 2007 Adam Jackson <ajax@redhat.com> 0.10.14-4
- BuildReq on libvisual and add the plugin. (#253491)

* Wed Aug 15 2007 - Bastien Nocera <bnocera@redhat.com> - 0.10.14-3
- Up requirement for liboil for PPC machines (#252179)

* Sat Aug 04 2007 - Bastien Nocera <bnocera@redhat.com> - 0.10.14-2
- Update to 0.10.14
- Add RTSP and SDP helper libraries

* Tue Jun 05 2007 - Bastien Nocera <bnocera@redhat.com> - 0.10.13-2
- Add missing files

* Tue Jun 05 2007 - Bastien Nocera <bnocera@redhat.com> - 0.10.13-1
- Update to 0.10.13

* Fri May 18 2007 Adam Jackson <ajax@redhat.com> 0.10.12-3
- Add directory ownership claims to %%files devel. (#240238)

* Thu Mar 08 2007 - Bastien Nocera <bnocera@redhat.com> - 0.10.12-2
- Remove the patch to disable docs, install the docs by hand instead
  Add libgstpbutils to the files

* Thu Mar 08 2007 - Bastien Nocera <bnocera@redhat.com> - 0.10.12-1
- Update to 0.10.12

* Wed Jan 24 2007 Adam Jackson <ajax@redhat.com>
- Minor spec cleanups (#186550)

* Tue Dec 12 2006 Matthias Clasen <mclasen@redhat.com> - 0.10.11-1
- Update to 0.10.11

* Mon Oct 23 2006 Matthias Clasen <mclasen@redhat.com> - 0.10.10-1
- Update to 0.10.10

* Fri Jul 28 2006 Matthias Clasen <mclasen@redhat.com> - 0.10.9-3
- Re-add docs

* Thu Jul 27 2006 Matthias Clasen <mclasen@redhat.com> - 0.10.9-2
- Disable gtk-doc to fix multilib conflicts

* Thu Jul 20 2006 John (J5) Palmieri <johnp@redhat.com> - 0.10.9-1
- Update to 0.10.9

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - sh: line 0: fg: no job control
- rebuild

* Mon May 22 2006 Matthias Clasen <mclasen@redhat.com> 0.10.7-1
- Update to 0.10.7

* Wed Mar 01 2006 Karsten Hopp <karsten@redhat.de> 0.10.3-3	
- really add BuildRequires: cdparanoia-devel (#179034)

* Mon Feb 20 2006 John (J5) Palmieri <johnp@redhat.com> - 0.10.3-2
- Obsolete gstreamer-plugins (Bug #182098)

* Fri Feb 10 2006 Christopher Aillon <caillon@redhat.com> - 0.10.3-1
- Update to 0.10.3

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 0.10.2-2.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Thu Feb 02 2006 Warren Togami <wtogami@redhat.com> - 0.10.2-2
- buildreq cdparanoia-devel (#179034 thias)

* Wed Jan 18 2006 John (J5) Palmieri <johnp@redhat.com> - 0.10.2-1
- Upgrade to 0.10.2
- Require gstreamer-0.10.2
- Add libgstcdda and libcdparanoia to the %files section

* Fri Jan 06 2006 John (J5) Palmieri <johnp@redhat.com> - 0.10.1-1
- New upstream version
- gst-launch removed from upstream

* Sat Dec 17 2005 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.10.0-1
- Fedora Development build

* Wed Dec 14 2005 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.10.0-0.gst.2
- new glib build

* Mon Dec 05 2005 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.10.0-0.gst.1
- new release

* Thu Dec 01 2005 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.9.7-0.gst.1
- new release with 0.10 majorminor
- remove sinesrc
- replace ximage with ximagesink
- update libs

* Sat Nov 12 2005 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.9.5-0.gst.1
- new release

* Mon Oct 24 2005 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.9.4-0.gst.1
- added audiotestsrc plugin
- new release

* Mon Oct 03 2005 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.9.3-0.gst.1
- new release

* Fri Sep 02 2005 Thomas Vander Stichele <thomas at apestaart dot org>
- clean up a little

* Fri May 6 2005 Christian Schaller <christian at fluendo dot com>
- Added libgstaudiorate and libgstsubparse to spec file

* Thu May 5 2005 Christian Schaller <christian at fluendo dot com>
- first attempt at spec file for gst-plugins-base
