#
# Conditional build:
%bcond_with    javac   # use javac instead of jikes
#
Summary:	Java Application Command Language
Summary(pl.UTF-8):	Java Application Command Language - język poleceń dla aplikacji
Name:		jacl
Version:	1.4.0
Release:	1
License:	BSD
Group:		Development/Languages/Java
Source0:	http://dl.sourceforge.net/tcljava/%{name}%{version}.tar.gz
# Source0-md5:	8ffe26a586ac6860d92811787fbc8544
URL:		http://tcljava.sourceforge.net/
BuildRequires:	jpackage-utils
BuildRequires:	rpmbuild(macros) >= 1.300
BuildRequires:	sed >= 4.0
BuildRequires:	jdk >= 1.4
ExclusiveArch:	i586 i686 pentium3 pentium4 athlon %{x8664} noarch
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Jacl (which stands for Java Application Command Language) is a
platform independent scripting language for Java. The feature set and
functionality of Jacl are structured to mirror the scripting language
Tcl version 8.0. In addition to the write-once-run-anywhere
philosophy, Jacl provides it's user with two other key concepts.
First, Jacl enables users to write Tcl extensions entirely in Java.
Extension writers can use the classes supplied in tcl.lang.*, as well
as any other classes, to write portable extensions. Second, Jacl
includes the Java Package, which provides a direct Tcl interface to
Java Objects. For example, the Java Package contains a Tcl command,
java::info, that provides a Jacl user with information about the
public methods, fields, etc. of a given Java class or object. The Java
Package enables the user to script Java.

%description -l pl.UTF-8
Jacl (czyli Java Application Command Language) to niezależny od
platformy język skryptowy dla Javy. Zbiór możliwości i funkcjonalność
Jacla mają odzwierciedlać język skryptowy Tcl w wersji 8.0. Oprócz
filozofii "napisać raz, uruchamiać wszędzie" Jacl udostępnia
użytkownikowi dwie inne kluczowe idee. Po pierwsze, Jacl pozwala na
pisanie rozszerzeń Tcl całkowicie w Javie. Piszący rozszerzenia mogą
używać klas dostarczonych w tcl.lang.*, a także dowolnych innych klas
do pisania przenośnych rozszerzeń. Po drugie, Jacl zawiera pakiet Java
udostępniający bezpośredni interfejs Tcl-a do obiektów Javy. Na
przykład pakiet Java zawiera polecenie Tcl java::info udostępniające
użytkownikowi Jacla informacje o publicznych metodach, polach itp.
danej klasy czy obiektu Javy. Pakiet Java pozwala używać Javy w sposób
skryptowy.

%prep
%setup -q -n %{name}%{version}

%build
unset CLASSPATH || :
export JAVA_HOME="%{java_home}"
%configure \
	--with-jdk="%{java_home}"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	BIN_INSTALL_DIR=$RPM_BUILD_ROOT%{_bindir} \
	XP_LIB_INSTALL_DIR=$RPM_BUILD_ROOT%{_javadir} \
	XP_TCLJAVA_INSTALL_DIR=$RPM_BUILD_ROOT%{_javadir}

sed -i -e 's,^XP_LIB_INSTALL_DIR=.*,XP_LIB_INSTALL_DIR="%{_javadir}",' \
	$RPM_BUILD_ROOT%{_bindir}/jaclsh

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README changes.txt diffs.txt known_issues.txt license.*
%attr(755,root,root) %{_bindir}/jaclsh
%attr(755,root,root) %{_bindir}/jdk.cfg
%attr(755,root,root) %{_bindir}/tjc
%{_javadir}/itcl.jar
%{_javadir}/itclsrc.jar
%{_javadir}/jacl.jar
%{_javadir}/jaclsrc.jar
%{_javadir}/janino.jar
%{_javadir}/janinosrc.jar
%{_javadir}/tcljava.jar
%{_javadir}/tcljavasrc.jar
%{_javadir}/tjc.jar
%{_javadir}/tjcsrc.jar
