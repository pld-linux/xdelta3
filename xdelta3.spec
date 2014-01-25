Summary:	XDELTA - version control system
Summary(es.UTF-8):	patch y diff para archivos binarios
Summary(pl.UTF-8):	XDELTA - system kontroli wersji
Summary(pt_BR.UTF-8):	patch e diff para arquivos binários
Name:		xdelta3
Version:	3.0.8
Release:	1
License:	GPL
Group:		Development/Version Control
#Source0Download: http://code.google.com/p/xdelta/downloads/list
Source0:	http://xdelta.googlecode.com/files/%{name}-%{version}.tar.xz
# Source0-md5:	c3ae3286ce4193de8e03d5bcaccf3bc3
Patch0:		patch-testing-regtest.cc.patch
URL:		http://www.xdelta.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib-devel >= 1.2.0
BuildRequires:	libtool
BuildRequires:	xz-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XDelta (X for XCF: the eXperimental Computing Facility at Berkeley) is
a library interface and binary delta generator (like a diff program
for binaries) and an RCS. These changes (deltas) are similar to the
output of the "diff" program in that they may be used to store and
transmit only the changes between files. However, unlike diff, the
output of XDelta is not expressed in a human-readable format - XDelta
can also also apply these deltas to a copy of the original file(s).
XDelta uses a fast, linear algorithm and performs well on both binary
and text files. XDelta typically outperforms GNU diff in both time and
generated-delta-size, even for plain text files. XDelta also includes
a simple implementation of the Rsync algorithm and several advanced
features for implementing RCS-like file-archival with.

The XDelta library performs its work independently of the actual
format used to encode the file and is intended to be used by various
higher-level programs such as XCF's Project Revision Control System
(PRCS). PRCS is a front end for a version control toolset. Xdelta uses
a binary file delta algorithm to replace the standard diff program
used by RCS.

%description -l es.UTF-8
xdelta es como las órdenes patch y diff, pero también funciona con
archivos binarios.

%description -l pl.UTF-8
XDelta (`X' od XCF - eXperimental Computing Facility w Berkeley) jest
biblioteką i generatorem binarnych delt (różnic podobnych do tych
tworzonych przez program diff, ale dla binariów) oraz systemem
kontroli wersji. Te zmiany (delty) są podobne do wyjścia programu diff
także w tym, że mogą być używane do przechowywania i transmisji tylko
zmian między plikami. Jednak, w przeciwieństwie do diffa, wyjście
XDelty nie jest wyrażone w postaci czytelnej dla człowieka; XDelta
może także nanieść te zmiany na kopię oryginalnego pliku (plików).
XDelta używa szybkiego, liniowego algorytmu i dobrze się sprawdza
zarówno na binarnych, jak i tekstowych plikach. Algorytm XDelta zwykle
jest wydajniejszy od GNU diffa zarówno pod względem czasu jak i
rozmiaru wygenerowanych różnic, nawet dla plików czysto tekstowych.
XDelta zawiera także przykładową implementację algorytmy Rsync i kilka
zaawansowanych możliwości do implementowania archiwizacji plików
podobnej do RCS.

Biblioteka XDelta działa dobrze niezależnie od formatu użytego przy
kodowaniu pliku i jest przeznaczona do używania w różnych
wysokopoziomowych programach takich jak system kontroli wersji z XCF
(PRCS - Project Revision Control System), będący frontendem do
zbioru narzędzi służących do kontroli wersji, w którym jest używany
algorytm binarnych różnic XDelta zamiast standardowego diffa używanego
przez RCS.

%description -l pt_BR.UTF-8
xdelta é como os comandos patch e diff, mas também funciona com
arquivos binários.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/xdelta3
%{_mandir}/man1/xdelta3*
