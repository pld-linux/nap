Summary:	Console napster client
Summary(pl):	Klient napstera pod konsole
Name:		nap
Version:	1.4.2
%define		short_ver	1.4
Release:	1
Group:		Applications/Communications
Group(pl):	Aplikacje/Komunikacja
Copyright:	Copyright (c) 2000 Kevin Sullivan (distributable)
Source0:	http://download.sourceforge.net/nap/%{name}-%{version}.tar.gz
URL:		http://sourceforge.net/projects/nap/
BuildRequires:	ncurses-devel >= 5.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A console napster client that can be compiled on almost any UNIX
machine. It includes basic scripting support and IRC support as well.

%description -l pl
Konsolowy klient napstera, który mo¿e byæ skompilowany na praktycznie
ka¿dej maszynie Unixowej. Zawiera podstawowe wsparcie dla tworzenia
w³asnych skryptów, podobnie jak wsparcie dla IRC.

%prep
%setup -q -n %{name}-%{short_ver}

%build
CFLAGS="-I/usr/include/ncurses $RPM_OPT_FLAGS"; export CFLAGS
LDFLAGS="-s" ; export LDFLAGS
%configure 

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz nap.conf.dist
%attr(755,root,root) %{_bindir}/*
