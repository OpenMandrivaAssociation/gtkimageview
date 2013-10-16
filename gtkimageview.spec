%define major	0
%define libname	%mklibname %{name} %{major}
%define devname	%mklibname %{name} -d

Summary:	Simple image viewer widget for GTK
Name:		gtkimageview
Version:	1.6.4
Release:	7
License:	LGPLv2+
Group:		System/Libraries
Url:		http://trac.bjourne.webfactional.com/
Source0:	http://trac.bjourne.webfactional.com/chrome/common/releases/%{name}-%{version}.tar.gz
# (fc) 1.3.0-1mdv disable -Werror flag
Patch0:		gtkimageview-1.3.0-nowerror.patch

BuildRequires:	gtk-doc
BuildRequires:	gnome-common
BuildRequires:	pkgconfig(gtk+-2.0)
Requires:	common-licenses

%description
GtkImageView is a widget that provides a zoomable and panable view of
a GdkPixbuf. It is intended to be usable in most types of image
viewing applications.

%package -n %{libname}
Summary:	Simple image viewer widget for GTK
Group:		System/Libraries

%description -n %{libname}
GtkImageView is a widget that provides a zoomable and panable view of
a GdkPixbuf. It is intended to be usable in most types of image
viewing applications.

This package contains the library needed to run programs dynamically
linked with gtkimageview.

%package -n %{devname}
Summary:	Static libraries and header files of %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
GtkImageView is a widget that provides a zoomable and panable view of
a GdkPixbuf. It is intended to be usable in most types of image
viewing applications.

%prep
%setup  -q
%apply_patches

%build
NOCONFIGURE=yes ./autogen.sh
%configure2_5x \
	--disable-static
%make LIBS="-lm"

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libgtkimageview.so.%{major}*

%files -n %{devname}
%doc README
%doc %{_datadir}/gtk-doc/html/*
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*

