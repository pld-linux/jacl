# TODO
# - resolve tcljava.jar conflict with tclBlend
#
# Conditional build:
%bcond_with    javac   # use javac instead of jikes
#
Summary:	Java Application Command Language
Summary(pl):	Java Application Command Language - jêzyk poleceñ dla aplikacji
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

%description -l pl
Jacl (czyli Java Application Command Language) to niezale¿ny od
platformy jêzyk skryptowy dla Javy. Zbiór mo¿liwo¶ci i funkcjonalno¶æ
Jacla maj± odzwierciedlaæ jêzyk skryptowy Tcl w wersji 8.0. Oprócz
filozofii "napisaæ raz, uruchamiaæ wszêdzie" Jacl udostêpnia
u¿ytkownikowi dwie inne kluczowe idee. Po pierwsze, Jacl pozwala na
pisanie rozszerzeñ Tcl ca³kowicie w Javie. Pisz±cy rozszerzenia mog±
u¿ywaæ klas dostarczonych w tcl.lang.*, a tak¿e dowolnych innych klas
do pisania przeno¶nych rozszerzeñ. Po drugie, Jacl zawiera pakiet Java
udostêpniaj±cy bezpo¶redni interfejs Tcl-a do obiektów Javy. Na
przyk³ad pakiet Java zawiera polecenie Tcl java::info udostêpniaj±ce
u¿ytkownikowi Jacla informacje o publicznych metodach, polach itp.
danej klasy czy obiektu Javy. Pakiet Java pozwala u¿ywaæ Javy w sposób
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
# XXX: dup with tclBlend
%{_javadir}/tcljava.jar
%{_javadir}/tcljavasrc.jar
%{_javadir}/tjc.jar
%{_javadir}/tjcsrc.jar
