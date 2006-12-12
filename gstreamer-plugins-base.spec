%define         gstreamer       gstreamer
%define         majorminor      0.10

%define         _gst            0.10.11

Name: 		%{gstreamer}-plugins-base
Version: 	0.10.11
Release:  	1%{?dist}	
Summary: 	GStreamer streaming media framework base plug-ins

Group: 		Applications/Multimedia
License: 	LGPL
URL:		http://gstreamer.freedesktop.org/
Source:         http://gstreamer.freedesktop.org/src/gst-plugins-base/gst-plugins-base-%{version}.tar.bz2
# http://bugzilla.gnome.org/show_bug.cgi?id=349099
Patch0:		gstreamer-plugins-base-0.10.9-docs.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:       %{gstreamer} >= %{_gst}
BuildRequires: 	%{gstreamer}-devel >= %{_gst}

BuildRequires:	liboil-devel >= 0.3.6
BuildRequires:  gettext
BuildRequires:  gcc-c++

BuildRequires:  gnome-vfs2-devel > 1.9.4.00
BuildRequires:  libogg-devel >= 1.0
BuildRequires:  libvorbis-devel >= 1.0
BuildRequires:  libtheora-devel >= 1.0
BuildRequires:  liboil-devel >= 0.3.2
BuildRequires:  alsa-lib-devel
BuildRequires:  pango-devel
BuildRequires:  libXv-devel
BuildRequires:  cdparanoia-devel
Obsoletes: gstreamer-plugins

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
%patch0 -p1 -b .docs

%build
%configure \
  --with-package-name='Fedora Core gstreamer-plugins-base package' \
  --with-package-origin='http://download.fedora.redhat.com/fedora' \
  --disable-gtk-doc

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall

# Clean out files that should not be part of the rpm.
rm -f $RPM_BUILD_ROOT%{_libdir}/gstreamer-%{majorminor}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/gstreamer-%{majorminor}/*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%find_lang gst-plugins-base-%{majorminor}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f gst-plugins-base-%{majorminor}.lang
%defattr(-, root, root)
%doc AUTHORS COPYING README REQUIREMENTS

# helper programs
%{_bindir}/gst-visualise-%{majorminor}
%{_mandir}/man1/gst-visualise-%{majorminor}*

# libraries
%{_libdir}/libgstinterfaces-%{majorminor}.so.*
%{_libdir}/libgstaudio-%{majorminor}.so.*
%{_libdir}/libgstriff-%{majorminor}.so.*
%{_libdir}/libgsttag-%{majorminor}.so.*
%{_libdir}/libgstnetbuffer-%{majorminor}.so.*
%{_libdir}/libgstrtp-%{majorminor}.so.*
%{_libdir}/libgstvideo-%{majorminor}.so.*
%{_libdir}/libgstcdda-0.10.so.*


# base plugins without external dependencies
%{_libdir}/gstreamer-%{majorminor}/libgstadder.so
%{_libdir}/gstreamer-%{majorminor}/libgstaudioconvert.so
%{_libdir}/gstreamer-%{majorminor}/libgstaudiotestsrc.so
%{_libdir}/gstreamer-%{majorminor}/libgstffmpegcolorspace.so
%{_libdir}/gstreamer-%{majorminor}/libgstdecodebin.so
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
%{_libdir}/gstreamer-%{majorminor}/libgstcdparanoia.so
%{_libdir}/gstreamer-%{majorminor}/libgstgdp.so

# base plugins with dependencies
%{_libdir}/gstreamer-%{majorminor}/libgstalsa.so
%{_libdir}/gstreamer-%{majorminor}/libgstgnomevfs.so
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
Obsoletes: gstreamer-plugins-devel

%description devel
GStreamer Base Plugins library development and header files.

%files devel
%defattr(-, root, root)
# plugin helper library headers
%{_includedir}/gstreamer-%{majorminor}/gst/audio/audio.h
%{_includedir}/gstreamer-%{majorminor}/gst/audio/gstaudiofilter.h
%{_includedir}/gstreamer-%{majorminor}/gst/audio/multichannel.h
%{_includedir}/gstreamer-%{majorminor}/gst/floatcast/floatcast.h
%{_includedir}/gstreamer-%{majorminor}/gst/riff/riff-ids.h
%{_includedir}/gstreamer-%{majorminor}/gst/riff/riff-media.h
%{_includedir}/gstreamer-%{majorminor}/gst/riff/riff-read.h
%{_includedir}/gstreamer-%{majorminor}/gst/video/video.h
%{_includedir}/gstreamer-%{majorminor}/gst/video/gstvideofilter.h
%{_includedir}/gstreamer-%{majorminor}/gst/video/gstvideosink.h
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
%{_includedir}/gstreamer-%{majorminor}/gst/interfaces/xoverlay.h
%{_includedir}/gstreamer-%{majorminor}/gst/audio/gstaudiosrc.h
%{_includedir}/gstreamer-%{majorminor}/gst/audio/gstbaseaudiosrc.h
%{_includedir}/gstreamer-%{majorminor}/gst/audio/multichannel-enumtypes.h
%{_includedir}/gstreamer-%{majorminor}/gst/rtp/gstrtpbuffer.h
%{_includedir}/gstreamer-%{majorminor}/gst/audio/gstaudioclock.h
%{_includedir}/gstreamer-%{majorminor}/gst/audio/gstaudiosink.h
%{_includedir}/gstreamer-%{majorminor}/gst/audio/gstbaseaudiosink.h
%{_includedir}/gstreamer-%{majorminor}/gst/audio/gstringbuffer.h
%{_includedir}/gstreamer-%{majorminor}/gst/netbuffer/gstnetbuffer.h
%{_includedir}/gstreamer-%{majorminor}/gst/tag/tag.h
%{_includedir}/gstreamer-%{majorminor}/gst/rtp/gstbasertpdepayload.h
%{_includedir}/gstreamer-%{majorminor}/gst/rtp/gstbasertppayload.h
%{_includedir}/gstreamer-%{majorminor}/gst/audio/mixerutils.h
%{_includedir}/gstreamer-%{majorminor}/gst/cdda/gstcddabasesrc.h
   

%{_libdir}/libgstaudio-%{majorminor}.so
%{_libdir}/libgstinterfaces-%{majorminor}.so
%{_libdir}/libgstnetbuffer-%{majorminor}.so
%{_libdir}/libgstriff-%{majorminor}.so
%{_libdir}/libgstrtp-%{majorminor}.so
%{_libdir}/libgsttag-%{majorminor}.so
%{_libdir}/libgstvideo-%{majorminor}.so
%{_libdir}/libgstcdda-0.10.so


# pkg-config files
%{_libdir}/pkgconfig/gstreamer-plugins-base-%{majorminor}.pc

# gtk-doc documentation
%doc %{_datadir}/gtk-doc/html/gst-plugins-base-libs-%{majorminor}
%doc %{_datadir}/gtk-doc/html/gst-plugins-base-plugins-%{majorminor}

%changelog
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
