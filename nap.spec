Summary:	Console napster client
Summary(pl):	Klient napstera pod konsole
Name:		nap
Version:	1.5.0
Release:	1
License:	distributable (Copyright (C) 2000 Kevin Sullivan)
Group:		Applications/Communications
Source0:	http://theory.stanford.edu/~selinger/nap/%{name}-%{version}.tar.gz
URL:		http://theory.stanford.edu/~selinger/software.html
BuildRequires:	autoconf
BuildRequires:	automake
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
%setup -q -n nap-%{version}

%build
CFLAGS="-I/usr/include/ncurses %{rpmcflags}"
rm -f missing
aclocal
autoconf
automake -a -c -f
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
%doc *.gz doc/*.html
%attr(755,root,root) %{_bindir}/*
