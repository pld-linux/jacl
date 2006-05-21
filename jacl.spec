# TODO: resolve tcljava.jar conflict with tclBlend
#
# Conditional build:
%bcond_with    javac   # use javac instead of jikes
#
%include /usr/lib/rpm/macros.java
Summary:	Java Application Command Language
Summary(pl):	Java Application Command Language - j�zyk polece� dla aplikacji
Name:		jacl
Version:	1.3.2
Release:	1
License:	BSD
Group:		Development/Languages/Java
Source0:	http://dl.sourceforge.net/tcljava/%{name}%{version}.tar.gz
# Source0-md5:	44ec6149e1664d4fc13651e9288dd2b6
URL:		http://tcljava.sourceforge.net/
BuildRequires:	sed >= 4.0
%if %{with javac}
BuildRequires:	jdk
ExclusiveArch:	i586 i686 pentium3 pentium4 athlon %{x8664} noarch
%else
BuildRequires:  jikes
%endif
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
Jacl (czyli Java Application Command Language) to niezale�ny od
platformy j�zyk skryptowy dla Javy. Zbi�r mo�liwo�ci i funkcjonalno��
Jacla maj� odzwierciedla� j�zyk skryptowy Tcl w wersji 8.0. Opr�cz
filozofii "napisa� raz, uruchamia� wsz�dzie" Jacl udost�pnia
u�ytkownikowi dwie inne kluczowe idee. Po pierwsze, Jacl pozwala na
pisanie rozszerze� Tcl ca�kowicie w Javie. Pisz�cy rozszerzenia mog�
u�ywa� klas dostarczonych w tcl.lang.*, a tak�e dowolnych innych klas
do pisania przeno�nych rozszerze�. Po drugie, Jacl zawiera pakiet Java
udost�pniaj�cy bezpo�redni interfejs Tcl-a do obiekt�w Javy. Na
przyk�ad pakiet Java zawiera polecenie Tcl java::info udost�pniaj�ce
u�ytkownikowi Jacla informacje o publicznych metodach, polach itp.
danej klasy czy obiektu Javy. Pakiet Java pozwala u�ywa� Javy w spos�b
skryptowy.

%prep
%setup -q -n %{name}%{version}

%build
unset CLASSPATH || :
export JAVA_HOME="%{java_home}"
%configure2_13 \
	   %{?with_javac:--without-jikes} \
	--with-jdk="%{java_home}"
%{__make} \
	   %{?with_javac:JAVAC_FLAGS="-g -source 1.4"}

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
%{_javadir}/jacl.jar
# XXX: dup with tclBlend
%{_javadir}/tcljava.jar
