%define lib_major	0
%define lib_name	%mklibname %{name} %{lib_major}
%define lib_name_devel	%mklibname %{name} -d

Summary:   Simple image viewer widget for GTK
Name:      gtkimageview
Version:   1.6.4
Release: 5
License:   LGPLv2+
Group:     System/Libraries
Source0:   http://trac.bjourne.webfactional.com/attachment/wiki/WikiStart/gtkimageview-%{version}.tar.gz
# (fc) 1.3.0-1mdv disable -Werror flag
Patch0:    gtkimageview-1.3.0-nowerror.patch
URL:       http://trac.bjourne.webfactional.com/
Requires:  common-licenses
BuildRequires: gtk+2-devel
BuildRequires: gtk-doc
BuildRequires: autoconf automake libtool
BuildRequires: gnome-common

%description
GtkImageView is a widget that provides a zoomable and panable view of
a GdkPixbuf. It is intended to be usable in most types of image
viewing applications.

%package -n %{lib_name}
Summary: %{summary}
Group: %{group}

%description -n %{lib_name}
GtkImageView is a widget that provides a zoomable and panable view of
a GdkPixbuf. It is intended to be usable in most types of image
viewing applications.

This package contains the library needed to run programs dynamically
linked with gtkimageview.

%package -n %{lib_name_devel}
Summary: Static libraries and header files of %{name}
Group:   Development/C
Requires:	%{lib_name} = %{version}
Provides: %{name}-devel = %{version}-%{release}

%description -n %{lib_name_devel}
GtkImageView is a widget that provides a zoomable and panable view of
a GdkPixbuf. It is intended to be usable in most types of image
viewing applications.

%prep
%setup  -q
%patch0 -p1 -b .nowerror

%build
NOCONFIGURE=yes ./autogen.sh
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

# cleanups
rm -rf %{buildroot}%{_libdir}/lib*.*a

%files -n %{lib_name}
%doc README
%{_libdir}/*.so.%{lib_major}*

%files -n %{lib_name_devel}
%doc %{_datadir}/gtk-doc/html/*
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*
