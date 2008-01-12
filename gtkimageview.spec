%define lib_major	0
%define lib_name	%mklibname %{name} %{lib_major}
%define lib_name_devel	%mklibname %{name} -d

Summary:   Simple image viewer widget for GTK
Name:      gtkimageview
Version:   1.3.0
Release: %mkrel 2
License:   LGPL
Group:     System/Libraries
Source0:   http://trac.bjourne.webfactional.com/attachment/wiki/WikiStart/gtkimageview-%{version}.tar.gz
# (fc) 1.3.0-1mdv disable -Werror flag
Patch0:    gtkimageview-1.3.0-nowerror.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-root
URL:       http://trac.bjourne.webfactional.com/
Requires:  common-licenses
BuildRequires: gtk+2-devel
BuildRequires: gtk-doc
BuildRequires: automake1.9
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

#needed by patch0
aclocal
automake
autoconf

%build

%configure2_5x

%make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %{lib_name} -p /sbin/ldconfig

%postun -n %{lib_name} -p /sbin/ldconfig

%files -n %{lib_name}
%defattr(-, root, root)
%doc README
%{_libdir}/*.so.%{lib_major}*

%files -n %{lib_name_devel}
%defattr(-, root, root)
%doc %{_datadir}/gtk-doc/html/*
%{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_libdir}/lib*.a
%{_libdir}/pkgconfig/*
%{_includedir}/*
