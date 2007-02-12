Summary:	Console napster client
Summary(pl.UTF-8):   Klient napstera pod konsole
Name:		nap
Version:	1.5.3
Release:	1
License:	distributable (Copyright (C) 2000 Kevin Sullivan)
Group:		Applications/Communications
Source0:	http://nap.sf.net/dist/%{name}-%{version}.tar.gz
# Source0-md5:	b39ceb2bac8432e1aef11b0d4ecf4c7c
URL:		http://nap.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	ncurses-devel >= 5.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A console napster client that can be compiled on almost any UNIX
machine. It includes basic scripting support and IRC support as well.

%description -l pl.UTF-8
Konsolowy klient napstera, który może być skompilowany na praktycznie
każdej maszynie uniksowej. Zawiera podstawowe wsparcie dla tworzenia
własnych skryptów, podobnie jak wsparcie dla IRC.

%prep
%setup -q

%build
CFLAGS="-I/usr/include/ncurses %{rpmcflags}"
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README doc/*.html
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
