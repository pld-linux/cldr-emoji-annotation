Summary:	Emoji annotation files in CLDR
Summary(pl.UTF-8):	Pliki adnotacji Emoji z CLDR
Name:		cldr-emoji-annotation
Version:	35.12.14971_0
Release:	1
# Annotation files are in Unicode license
License:	LGPL v2+, Unicode
Group:		Libraries
#Source0Download: https://github.com/fujiwarat/cldr-emoji-annotation/releases
Source0:	https://github.com/fujiwarat/cldr-emoji-annotation/releases/download/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	9d9b5d7fba5651d64d4823577acaca09
URL:		https://github.com/fujiwarat/cldr-emoji-annotation
BuildRequires:	rpmbuild(macros) >= 1.446
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides the emoji annotation file by language in CLDR.

%description -l pl.UTF-8
Ten pakiet zawiera plik adnotacji piktogramów (emoji) wg języków z
CLDR.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	INSTALL="install -p"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README unicode-license.txt
%dir %{_datadir}/unicode
%dir %{_datadir}/unicode/cldr
%dir %{_datadir}/unicode/cldr/common
%{_datadir}/unicode/cldr/common/annotations
%{_datadir}/unicode/cldr/common/annotationsDerived
%{_npkgconfigdir}/cldr-emoji-annotation.pc
