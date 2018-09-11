#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : doxygen
Version  : 1.8.14
Release  : 8
URL      : ftp://ftp.stack.nl/pub/users/dimitri/doxygen-1.8.14.src.tar.gz
Source0  : ftp://ftp.stack.nl/pub/users/dimitri/doxygen-1.8.14.src.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 QPL-1.0
Requires: doxygen-bin
Requires: doxygen-license
BuildRequires : bison
BuildRequires : bison-dev
BuildRequires : buildreq-cmake
BuildRequires : cmake(Clang)
BuildRequires : cmake(LLVM)
BuildRequires : doxygen
BuildRequires : flex
BuildRequires : glibc-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(sqlite3)
BuildRequires : python-dev
BuildRequires : python3
BuildRequires : qtbase-dev mesa-dev
BuildRequires : zlib-dev

%description
This directory contains a small subset of Troll-Tech's Qt library
The subset is enough to build the doxygen executable, but lacks many of
the features found in the Qt library. See http://www.trolltech.com
for the full package.

%package bin
Summary: bin components for the doxygen package.
Group: Binaries
Requires: doxygen-license

%description bin
bin components for the doxygen package.


%package license
Summary: license components for the doxygen package.
Group: Default

%description license
license components for the doxygen package.


%prep
%setup -q -n doxygen-1.8.14

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1536631570
mkdir -p clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags}
popd

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
cd clr-build; make test || :

%install
export SOURCE_DATE_EPOCH=1536631570
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/doxygen
cp LICENSE %{buildroot}/usr/share/doc/doxygen/LICENSE
cp qtools/LICENSE.GPL %{buildroot}/usr/share/doc/doxygen/qtools_LICENSE.GPL
cp qtools/LICENSE.QPL %{buildroot}/usr/share/doc/doxygen/qtools_LICENSE.QPL
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/doxygen

%files license
%defattr(-,root,root,-)
/usr/share/doc/doxygen/LICENSE
/usr/share/doc/doxygen/qtools_LICENSE.GPL
/usr/share/doc/doxygen/qtools_LICENSE.QPL
