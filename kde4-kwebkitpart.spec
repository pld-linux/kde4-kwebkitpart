
%define		qtver		4.8.4
%define		kdever		4.10.2
%define		snap		20130415
%define		orgname		kwebkitpart

%define		rel	1
Summary:	kde4-kwebkitpart - QWebkit plugin
Name:		kde4-kwebkitpart
Version:	%{kdever}
Release:	0.%{snap}.%{rel}
License:	GPL v2
Group:		X11/Libraries
# git clone git://anongit.kde.org/kwebkitpart
Source0:	%{orgname}-%{snap}.tar.bz2
# Source0-md5:	b0c8afbeaf30937b551ef8598b316af5
BuildRequires:	QtCore-devel >= %{qtver}
BuildRequires:	QtSvg-devel >= %{qtver}
BuildRequires:	QtUiTools-devel >= %{qtver}
BuildRequires:	QtWebKit-devel >= %{qtver}
BuildRequires:	automoc4
BuildRequires:	cmake >= 2.8.0
BuildRequires:	kde4-kdelibs-devel >= %{kdever}
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.600
Obsoletes:	webkitkde
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KDE part library to use QtWebkit instread of KHTML. It works as plugin
for Konqueror.

%prep
%setup -q -n %{orgname}-%{snap}

%build
install -d build
cd build
%cmake \
	../

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
%attr(755,root,root) %{_libdir}/kde4/kwebkitpart.so
%{_iconsdir}/hicolor/*x*/apps/webkit.png
%{_datadir}/kde4/services/kwebkitpart.desktop
%{_datadir}/apps/kwebkitpart
