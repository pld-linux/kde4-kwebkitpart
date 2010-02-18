
%define		qtver		4.6.2
%define		kdever		4.4.0
%define		snap		1092287
%define		orgname		kwebkitpart

Summary:	kde4-kwebkitpart - QWebkit plugin
Name:		kde4-kwebkitpart
Version:	0
Release:	0.%{snap}.1
License:	GPL v2
Group:		X11/Libraries
# svn co svn://anonsvn.kde.org/home/kde/trunk/extragear/base/kwebkitpart
Source0:	%{orgname}-%{snap}.tar.bz2
# Source0-md5:	f46c4e8eaeb5751877474790d349fe84
BuildRequires:	QtCore-devel >= %{qtver}
BuildRequires:	QtSvg-devel >= %{qtver}
BuildRequires:	QtUiTools-devel >= %{qtver}
BuildRequires:	QtWebKit-devel >= %{qtver}
BuildRequires:	automoc4
BuildRequires:	cmake >= 2.8.0
BuildRequires:	kde4-kdelibs-devel >= %{kdever}
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.293
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KDE part library to use QtWebkit instread of KHTML. It works as plugin
for Konqueror.

%package devel
Summary:	Header files for webkitkde library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki webkitkde
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for kwebkitpart.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla kwebkitpart.

%prep
%setup -q -n %{orgname}-%{snap}

%build
install -d build
cd build
%cmake .. \
	-DCMAKE_BUILD_TYPE=%{!?debug:Release}%{?debug:Debug} \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64
%endif

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkdewebkit.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkdewebkit.so.?
%attr(755,root,root) %{_libdir}/libwebkitkde.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwebkitkde.so.?
%attr(755,root,root) %{_libdir}/kde4/webkitkdepart.so
%{_datadir}/kde4/services/webkitpart.desktop
%{_datadir}/apps/webkitpart
%{_iconsdir}/*/*/*/*.png

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkdewebkit.so
%attr(755,root,root) %{_libdir}/libwebkitkde.so
%{_includedir}/KDE/KdeWebKit
%{_includedir}/KDE/WebKitPart
%{_includedir}/kdewebkit
%{_includedir}/webkitkde
%{_datadir}/apps/cmake/modules/*.cmake
