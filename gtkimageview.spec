%define lib_major	0
%define lib_name	%mklibname %{name} %{lib_major}
%define lib_name_devel	%mklibname %{name} -d

Summary:	Simple image viewer widget for GTK
Name:		gtkimageview
Version:	1.6.4
Release:	5
License:	LGPLv2+
Group:		System/Libraries
URL:		http://trac.bjourne.webfactional.com/
Source0:	http://trac.bjourne.webfactional.com/attachment/wiki/WikiStart/gtkimageview-%{version}.tar.gz
# (fc) 1.3.0-1mdv disable -Werror flag
Patch0:		gtkimageview-1.3.0-nowerror.patch
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	gtk-doc
BuildRequires:	automake1.9
BuildRequires:	gnome-common
Requires:	common-licenses

%description
GtkImageView is a widget that provides a zoomable and panable view of
a GdkPixbuf. It is intended to be usable in most types of image
viewing applications.

%package -n %{lib_name}
Summary:	Simple image viewer widget for GTK
Group:		System/Libraries

%description -n %{lib_name}
GtkImageView is a widget that provides a zoomable and panable view of
a GdkPixbuf. It is intended to be usable in most types of image
viewing applications.

This package contains the library needed to run programs dynamically
linked with gtkimageview.

%package -n %{lib_name_devel}
Summary:	Static libraries and header files of %{name}
Group:		Development/C
Requires:	%{lib_name} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{lib_name_devel}
GtkImageView is a widget that provides a zoomable and panable view of
a GdkPixbuf. It is intended to be usable in most types of image
viewing applications.

%prep
%setup  -q
%patch0 -p1 -b .nowerror

%build
NOCONFIGURE=yes ./autogen.sh
%configure2_5x --disable-static
%make LIBS="-lm"

%install
%makeinstall_std

%files -n %{lib_name}
%doc README
%{_libdir}/*.so.%{lib_major}*

%files -n %{lib_name_devel}
%doc %{_datadir}/gtk-doc/html/*
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*


%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 1.6.4-4mdv2011.0
+ Revision: 664954
- mass rebuild

* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 1.6.4-3mdv2011.0
+ Revision: 605511
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 1.6.4-2mdv2010.1
+ Revision: 522811
- rebuilt for 2010.1

* Thu Aug 06 2009 Funda Wang <fwang@mandriva.org> 1.6.4-1mdv2010.0
+ Revision: 410552
- use autogen rather thant autoreconf
- new version 1.6.4

* Sun Mar 15 2009 Funda Wang <fwang@mandriva.org> 1.6.3-1mdv2009.1
+ Revision: 355265
- New version 1.6.3

* Sun Nov 09 2008 Oden Eriksson <oeriksson@mandriva.com> 1.6.1-3mdv2009.1
+ Revision: 301491
- rebuilt against new libxcb

* Wed Aug 06 2008 Thierry Vignaud <tv@mandriva.org> 1.6.1-2mdv2009.0
+ Revision: 264645
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Sat May 17 2008 Funda Wang <fwang@mandriva.org> 1.6.1-1mdv2009.0
+ Revision: 208525
- New version 1.6.1

* Sun Feb 03 2008 Funda Wang <fwang@mandriva.org> 1.5.0-1mdv2008.1
+ Revision: 161838
- New version 1.5.0

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Jul 31 2007 Frederic Crozat <fcrozat@mandriva.com> 1.3.0-1mdv2008.0
+ Revision: 57004
- Import gtkimageview

