#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v2
# autospec commit: f032afc72f6d
#
Name     : doxygen
Version  : 1.9.8
Release  : 16
URL      : https://sourceforge.net/projects/doxygen/files/rel-1.9.8/doxygen-1.9.8.src.tar.gz
Source0  : https://sourceforge.net/projects/doxygen/files/rel-1.9.8/doxygen-1.9.8.src.tar.gz
Summary  : Tool for generating documentation from annotated source code
Group    : Development/Tools
License  : GPL-2.0 MIT
Requires: doxygen-bin = %{version}-%{release}
Requires: doxygen-license = %{version}-%{release}
BuildRequires : bison
BuildRequires : bison-dev
BuildRequires : buildreq-cmake
BuildRequires : doxygen
BuildRequires : flex
BuildRequires : fmt-dev
BuildRequires : glibc-dev
BuildRequires : libxml2
BuildRequires : llvm-dev
BuildRequires : python3
BuildRequires : qtbase-dev
BuildRequires : qtbase-dev mesa-dev
BuildRequires : spdlog-dev
BuildRequires : zlib-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Doxygen is the de facto standard tool for generating documentation from
annotated C++ sources, but it also supports other popular programming languages
such as C, Objective-C, C#, PHP, Java, Python, IDL (Corba, Microsoft, and
UNO/OpenOffice flavors), Fortran, VHDL and to some extent D.

%package bin
Summary: bin components for the doxygen package.
Group: Binaries
Requires: doxygen-license = %{version}-%{release}

%description bin
bin components for the doxygen package.


%package license
Summary: license components for the doxygen package.
Group: Default

%description license
license components for the doxygen package.


%prep
%setup -q -n doxygen-1.9.8
cd %{_builddir}/doxygen-1.9.8

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1697738602
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
%cmake .. -DBUILD_SHARED_LIBS=OFF \
-DMAN_INSTALL_DIR=/usr/share/man/man1
make  %{?_smp_mflags}
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
cd clr-build; make test || :

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1697738602
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/doxygen
cp %{_builddir}/doxygen-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/doxygen/4cc77b90af91e615a64ae04893fdffa7939db84c || :
cp %{_builddir}/doxygen-%{version}/addon/doxmlparser/LICENSE %{buildroot}/usr/share/package-licenses/doxygen/d7a0ab20a59a1fc0606c61c1f82c3c060bec0a93 || :
cp %{_builddir}/doxygen-%{version}/deps/libmscgen/COPYING %{buildroot}/usr/share/package-licenses/doxygen/bca27f784110bf4696bad645f60ee7361dd96ea7 || :
cp %{_builddir}/doxygen-%{version}/deps/spdlog/LICENSE %{buildroot}/usr/share/package-licenses/doxygen/617ee17d495e6cb87f0d74cc2bddffaf5b827b1f || :
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/doxygen

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/doxygen/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/doxygen/617ee17d495e6cb87f0d74cc2bddffaf5b827b1f
/usr/share/package-licenses/doxygen/bca27f784110bf4696bad645f60ee7361dd96ea7
/usr/share/package-licenses/doxygen/d7a0ab20a59a1fc0606c61c1f82c3c060bec0a93
