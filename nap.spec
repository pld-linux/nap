Summary:	Console napster client
Summary(pl):	Klient napstera pod konsole
Name:		nap
Version:	1.4.4ps9
Release:	1
License:	Distributable (Copyright (c) 2000 Kevin Sullivan)
Group:		Applications/Communications
Group(de):	Applikationen/Kommunikation
Group(pl):	Aplikacje/Komunikacja
Source0:	http://theory.stanford.edu/~selinger/nap/%{name}-1.4.4-ps9.tar.gz
URL:		http://theory.stanford.edu/~selinger/software.html
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
%setup -q -n nap-1.4.4-ps9

%build
CFLAGS="-I/usr/include/ncurses %{rpmcflags}"
%configure 

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README ChangeLog AUTHORS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz *.html
%attr(755,root,root) %{_bindir}/*
