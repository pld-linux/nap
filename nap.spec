Summary:	Console napster client
Summary(pl):	Klient napstera pod konsole
Name:		nap
Version:	1.4.4ps7
Release:	1
Group:		Applications/Communications
Group(de):	Applikationen/Kommunikation
Group(pl):	Aplikacje/Komunikacja
Copyright:	Copyright (c) 2000 Kevin Sullivan (distributable)
Source0:	http://theory.stanford.edu/~selinger/nap/%{name}-1.4.4-ps8.tar.gz
URL:		http://theory.stanford.edu/~selinger/software.html
BuildRequires:	ncurses-devel >= 5.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A console napster client that can be compiled on almost any UNIX
machine. It includes basic scripting support and IRC support as well.

%description -l pl
Konsolowy klient napstera, kt�ry mo�e by� skompilowany na praktycznie
ka�dej maszynie Unixowej. Zawiera podstawowe wsparcie dla tworzenia
w�asnych skrypt�w, podobnie jak wsparcie dla IRC.

%prep
%setup -q -n nap-1.4.4-ps8

%build
CFLAGS="-I/usr/include/ncurses %{!?debug:$RPM_OPT_FLAGS}%{?debug:-O0 -g}"
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
