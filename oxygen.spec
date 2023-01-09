#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xD7574483BB57B18D (jr@jriddell.org)
#
Name     : oxygen
Version  : 5.26.5
Release  : 78
URL      : https://download.kde.org/stable/plasma/5.26.5/oxygen-5.26.5.tar.xz
Source0  : https://download.kde.org/stable/plasma/5.26.5/oxygen-5.26.5.tar.xz
Source1  : https://download.kde.org/stable/plasma/5.26.5/oxygen-5.26.5.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : CC0-1.0 GPL-2.0 GPL-3.0 LGPL-2.0 LGPL-2.1 LGPL-3.0 MIT
Requires: oxygen-bin = %{version}-%{release}
Requires: oxygen-data = %{version}-%{release}
Requires: oxygen-lib = %{version}-%{release}
Requires: oxygen-license = %{version}-%{release}
Requires: oxygen-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules pkgconfig(xcb) xcb-util-cursor-dev xcb-util-image-dev xcb-util-keysyms-dev xcb-util-renderutil-dev xcb-util-wm-dev xcb-util-dev
BuildRequires : extra-cmake-modules-data
BuildRequires : frameworkintegration-dev
BuildRequires : kcmutils-dev
BuildRequires : kconfigwidgets-dev
BuildRequires : kdecoration-dev
BuildRequires : ki18n-dev
BuildRequires : kwayland-dev
BuildRequires : qtbase-dev mesa-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
oxygen-style-animated is a branch of trunk/KDE/kdebase/runtime/kstyles/oxygen that introduces smooth animations for the Oxygen widget style.

%package bin
Summary: bin components for the oxygen package.
Group: Binaries
Requires: oxygen-data = %{version}-%{release}
Requires: oxygen-license = %{version}-%{release}

%description bin
bin components for the oxygen package.


%package data
Summary: data components for the oxygen package.
Group: Data

%description data
data components for the oxygen package.


%package lib
Summary: lib components for the oxygen package.
Group: Libraries
Requires: oxygen-data = %{version}-%{release}
Requires: oxygen-license = %{version}-%{release}

%description lib
lib components for the oxygen package.


%package license
Summary: license components for the oxygen package.
Group: Default

%description license
license components for the oxygen package.


%package locales
Summary: locales components for the oxygen package.
Group: Default

%description locales
locales components for the oxygen package.


%prep
%setup -q -n oxygen-5.26.5
cd %{_builddir}/oxygen-5.26.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1673303598
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1673303598
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/oxygen
cp %{_builddir}/oxygen-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/oxygen/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/oxygen-%{version}/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/oxygen/3e8971c6c5f16674958913a94a36b1ea7a00ac46 || :
cp %{_builddir}/oxygen-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/oxygen/3e8971c6c5f16674958913a94a36b1ea7a00ac46 || :
cp %{_builddir}/oxygen-%{version}/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/oxygen/2123756e0b1fc8243547235a33c0fcabfe3b9a51 || :
cp %{_builddir}/oxygen-%{version}/LICENSES/GPL-3.0-or-later.txt %{buildroot}/usr/share/package-licenses/oxygen/e3bdbf20d43fc066a1b40a64d57d4ae5a31f177f || :
cp %{_builddir}/oxygen-%{version}/LICENSES/LGPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/oxygen/a4c60b3fefda228cd7439d3565df043192fef137 || :
cp %{_builddir}/oxygen-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/oxygen/a4c60b3fefda228cd7439d3565df043192fef137 || :
cp %{_builddir}/oxygen-%{version}/LICENSES/LGPL-2.1-only.txt %{buildroot}/usr/share/package-licenses/oxygen/81b58c89ceef8e9f8bd5d00a287edbd15f9d3567 || :
cp %{_builddir}/oxygen-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/oxygen/19d98e1b6f8ef12849ea4012a052d3907f336c91 || :
cp %{_builddir}/oxygen-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/oxygen/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/oxygen-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/oxygen/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/oxygen-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/oxygen/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/oxygen-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/oxygen/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/oxygen-%{version}/LICENSES/MIT.txt %{buildroot}/usr/share/package-licenses/oxygen/81e12d0c07782abcf558af7aa19846e3e2606a70 || :
cp %{_builddir}/oxygen-%{version}/cursors/LICENSE %{buildroot}/usr/share/package-licenses/oxygen/e7d563f52bf5295e6dba1d67ac23e9f6a160fab9 || :
pushd clr-build
%make_install
popd
%find_lang oxygen_style_config
%find_lang oxygen_style_demo
%find_lang liboxygenstyleconfig
%find_lang oxygen_kdecoration

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/oxygen-demo5
/usr/bin/oxygen-settings5

%files data
%defattr(-,root,root,-)
/usr/share/color-schemes/Oxygen.colors
/usr/share/color-schemes/OxygenCold.colors
/usr/share/icons/KDE_Classic/cursors/00000000000000020006000e7e9ffc3f
/usr/share/icons/KDE_Classic/cursors/00008160000006810000408080010102
/usr/share/icons/KDE_Classic/cursors/08e8e1c95fe2fc01f976f1e063a24ccd
/usr/share/icons/KDE_Classic/cursors/3ecb610c1bf2410f44200f48c40d3599
/usr/share/icons/KDE_Classic/cursors/4498f0e0c1937ffe01fd06f973665830
/usr/share/icons/KDE_Classic/cursors/5c6cd98b3f3ebcb1f9c7f1c204630408
/usr/share/icons/KDE_Classic/cursors/9081237383d90e509aa00f00170e968f
/usr/share/icons/KDE_Classic/cursors/9d800788f1b08800ae810202380a0822
/usr/share/icons/KDE_Classic/cursors/X_cursor
/usr/share/icons/KDE_Classic/cursors/all-scroll
/usr/share/icons/KDE_Classic/cursors/bottom_left_corner
/usr/share/icons/KDE_Classic/cursors/bottom_right_corner
/usr/share/icons/KDE_Classic/cursors/bottom_side
/usr/share/icons/KDE_Classic/cursors/center_ptr
/usr/share/icons/KDE_Classic/cursors/closedhand
/usr/share/icons/KDE_Classic/cursors/col-resize
/usr/share/icons/KDE_Classic/cursors/cross
/usr/share/icons/KDE_Classic/cursors/crossed_circle
/usr/share/icons/KDE_Classic/cursors/crosshair
/usr/share/icons/KDE_Classic/cursors/d9ce0ab605698f320427677b458ad60b
/usr/share/icons/KDE_Classic/cursors/dnd-move
/usr/share/icons/KDE_Classic/cursors/dnd-no-drop
/usr/share/icons/KDE_Classic/cursors/dnd-none
/usr/share/icons/KDE_Classic/cursors/e-resize
/usr/share/icons/KDE_Classic/cursors/e29285e634086352946a0e7090d73106
/usr/share/icons/KDE_Classic/cursors/fcf21c00b30f7e3f83fe0dfd12e71cff
/usr/share/icons/KDE_Classic/cursors/fleur
/usr/share/icons/KDE_Classic/cursors/forbidden
/usr/share/icons/KDE_Classic/cursors/half-busy
/usr/share/icons/KDE_Classic/cursors/hand1
/usr/share/icons/KDE_Classic/cursors/hand2
/usr/share/icons/KDE_Classic/cursors/help
/usr/share/icons/KDE_Classic/cursors/ibeam
/usr/share/icons/KDE_Classic/cursors/left_ptr
/usr/share/icons/KDE_Classic/cursors/left_ptr_watch
/usr/share/icons/KDE_Classic/cursors/left_side
/usr/share/icons/KDE_Classic/cursors/move
/usr/share/icons/KDE_Classic/cursors/n-resize
/usr/share/icons/KDE_Classic/cursors/ne-resize
/usr/share/icons/KDE_Classic/cursors/nesw-resize
/usr/share/icons/KDE_Classic/cursors/not-allowed
/usr/share/icons/KDE_Classic/cursors/nw-resize
/usr/share/icons/KDE_Classic/cursors/nwse-resize
/usr/share/icons/KDE_Classic/cursors/openhand
/usr/share/icons/KDE_Classic/cursors/pirate
/usr/share/icons/KDE_Classic/cursors/pointer
/usr/share/icons/KDE_Classic/cursors/pointing_hand
/usr/share/icons/KDE_Classic/cursors/progress
/usr/share/icons/KDE_Classic/cursors/question_arrow
/usr/share/icons/KDE_Classic/cursors/right_ptr
/usr/share/icons/KDE_Classic/cursors/right_side
/usr/share/icons/KDE_Classic/cursors/row-resize
/usr/share/icons/KDE_Classic/cursors/s-resize
/usr/share/icons/KDE_Classic/cursors/sb_h_double_arrow
/usr/share/icons/KDE_Classic/cursors/sb_v_double_arrow
/usr/share/icons/KDE_Classic/cursors/se-resize
/usr/share/icons/KDE_Classic/cursors/size_all
/usr/share/icons/KDE_Classic/cursors/size_bdiag
/usr/share/icons/KDE_Classic/cursors/size_fdiag
/usr/share/icons/KDE_Classic/cursors/size_hor
/usr/share/icons/KDE_Classic/cursors/size_ver
/usr/share/icons/KDE_Classic/cursors/split_h
/usr/share/icons/KDE_Classic/cursors/split_v
/usr/share/icons/KDE_Classic/cursors/sw-resize
/usr/share/icons/KDE_Classic/cursors/text
/usr/share/icons/KDE_Classic/cursors/top_left_corner
/usr/share/icons/KDE_Classic/cursors/top_right_corner
/usr/share/icons/KDE_Classic/cursors/top_side
/usr/share/icons/KDE_Classic/cursors/up_arrow
/usr/share/icons/KDE_Classic/cursors/v_double_arrow
/usr/share/icons/KDE_Classic/cursors/w-resize
/usr/share/icons/KDE_Classic/cursors/wait
/usr/share/icons/KDE_Classic/cursors/watch
/usr/share/icons/KDE_Classic/cursors/whats_this
/usr/share/icons/KDE_Classic/cursors/xcursorconfig
/usr/share/icons/KDE_Classic/cursors/xterm
/usr/share/icons/KDE_Classic/index.theme
/usr/share/icons/Oxygen_Black/cursors/00000000000000020006000e7e9ffc3f
/usr/share/icons/Oxygen_Black/cursors/00008160000006810000408080010102
/usr/share/icons/Oxygen_Black/cursors/03b6e0fcb3499374a867c041f52298f0
/usr/share/icons/Oxygen_Black/cursors/08e8e1c95fe2fc01f976f1e063a24ccd
/usr/share/icons/Oxygen_Black/cursors/1081e37283d90000800003c07f3ef6bf
/usr/share/icons/Oxygen_Black/cursors/3085a0e285430894940527032f8b26df
/usr/share/icons/Oxygen_Black/cursors/3ecb610c1bf2410f44200f48c40d3599
/usr/share/icons/Oxygen_Black/cursors/4498f0e0c1937ffe01fd06f973665830
/usr/share/icons/Oxygen_Black/cursors/5c6cd98b3f3ebcb1f9c7f1c204630408
/usr/share/icons/Oxygen_Black/cursors/6407b0e94181790501fd1e167b474872
/usr/share/icons/Oxygen_Black/cursors/640fb0e74195791501fd1ed57b41487f
/usr/share/icons/Oxygen_Black/cursors/9081237383d90e509aa00f00170e968f
/usr/share/icons/Oxygen_Black/cursors/9d800788f1b08800ae810202380a0822
/usr/share/icons/Oxygen_Black/cursors/X_cursor
/usr/share/icons/Oxygen_Black/cursors/a2a266d0498c3104214a47bd64ab0fc8
/usr/share/icons/Oxygen_Black/cursors/alias
/usr/share/icons/Oxygen_Black/cursors/all-scroll
/usr/share/icons/Oxygen_Black/cursors/b66166c04f8c3109214a4fbd64a50fc8
/usr/share/icons/Oxygen_Black/cursors/circle
/usr/share/icons/Oxygen_Black/cursors/closedhand
/usr/share/icons/Oxygen_Black/cursors/col-resize
/usr/share/icons/Oxygen_Black/cursors/color-picker
/usr/share/icons/Oxygen_Black/cursors/copy
/usr/share/icons/Oxygen_Black/cursors/cross
/usr/share/icons/Oxygen_Black/cursors/crossed_circle
/usr/share/icons/Oxygen_Black/cursors/d9ce0ab605698f320427677b458ad60b
/usr/share/icons/Oxygen_Black/cursors/dnd-copy
/usr/share/icons/Oxygen_Black/cursors/dnd-link
/usr/share/icons/Oxygen_Black/cursors/dnd-move
/usr/share/icons/Oxygen_Black/cursors/dnd-no-drop
/usr/share/icons/Oxygen_Black/cursors/dnd-none
/usr/share/icons/Oxygen_Black/cursors/e-resize
/usr/share/icons/Oxygen_Black/cursors/e29285e634086352946a0e7090d73106
/usr/share/icons/Oxygen_Black/cursors/fcf21c00b30f7e3f83fe0dfd12e71cff
/usr/share/icons/Oxygen_Black/cursors/fleur
/usr/share/icons/Oxygen_Black/cursors/forbidden
/usr/share/icons/Oxygen_Black/cursors/half-busy
/usr/share/icons/Oxygen_Black/cursors/hand1
/usr/share/icons/Oxygen_Black/cursors/hand2
/usr/share/icons/Oxygen_Black/cursors/help
/usr/share/icons/Oxygen_Black/cursors/ibeam
/usr/share/icons/Oxygen_Black/cursors/left_ptr
/usr/share/icons/Oxygen_Black/cursors/left_ptr_watch
/usr/share/icons/Oxygen_Black/cursors/link
/usr/share/icons/Oxygen_Black/cursors/move
/usr/share/icons/Oxygen_Black/cursors/n-resize
/usr/share/icons/Oxygen_Black/cursors/ne-resize
/usr/share/icons/Oxygen_Black/cursors/nesw-resize
/usr/share/icons/Oxygen_Black/cursors/not-allowed
/usr/share/icons/Oxygen_Black/cursors/nw-resize
/usr/share/icons/Oxygen_Black/cursors/nwse-resize
/usr/share/icons/Oxygen_Black/cursors/openhand
/usr/share/icons/Oxygen_Black/cursors/pencil
/usr/share/icons/Oxygen_Black/cursors/pirate
/usr/share/icons/Oxygen_Black/cursors/plus
/usr/share/icons/Oxygen_Black/cursors/pointer
/usr/share/icons/Oxygen_Black/cursors/pointing_hand
/usr/share/icons/Oxygen_Black/cursors/progress
/usr/share/icons/Oxygen_Black/cursors/question_arrow
/usr/share/icons/Oxygen_Black/cursors/row-resize
/usr/share/icons/Oxygen_Black/cursors/s-resize
/usr/share/icons/Oxygen_Black/cursors/sb_h_double_arrow
/usr/share/icons/Oxygen_Black/cursors/sb_v_double_arrow
/usr/share/icons/Oxygen_Black/cursors/se-resize
/usr/share/icons/Oxygen_Black/cursors/size_all
/usr/share/icons/Oxygen_Black/cursors/size_bdiag
/usr/share/icons/Oxygen_Black/cursors/size_fdiag
/usr/share/icons/Oxygen_Black/cursors/size_hor
/usr/share/icons/Oxygen_Black/cursors/size_ver
/usr/share/icons/Oxygen_Black/cursors/split_h
/usr/share/icons/Oxygen_Black/cursors/split_v
/usr/share/icons/Oxygen_Black/cursors/sw-resize
/usr/share/icons/Oxygen_Black/cursors/text
/usr/share/icons/Oxygen_Black/cursors/up_arrow
/usr/share/icons/Oxygen_Black/cursors/v_double_arrow
/usr/share/icons/Oxygen_Black/cursors/w-resize
/usr/share/icons/Oxygen_Black/cursors/wait
/usr/share/icons/Oxygen_Black/cursors/watch
/usr/share/icons/Oxygen_Black/cursors/whats_this
/usr/share/icons/Oxygen_Black/cursors/xterm
/usr/share/icons/Oxygen_Black/index.theme
/usr/share/icons/Oxygen_Blue/cursors/00000000000000020006000e7e9ffc3f
/usr/share/icons/Oxygen_Blue/cursors/00008160000006810000408080010102
/usr/share/icons/Oxygen_Blue/cursors/03b6e0fcb3499374a867c041f52298f0
/usr/share/icons/Oxygen_Blue/cursors/08e8e1c95fe2fc01f976f1e063a24ccd
/usr/share/icons/Oxygen_Blue/cursors/1081e37283d90000800003c07f3ef6bf
/usr/share/icons/Oxygen_Blue/cursors/3085a0e285430894940527032f8b26df
/usr/share/icons/Oxygen_Blue/cursors/3ecb610c1bf2410f44200f48c40d3599
/usr/share/icons/Oxygen_Blue/cursors/4498f0e0c1937ffe01fd06f973665830
/usr/share/icons/Oxygen_Blue/cursors/5c6cd98b3f3ebcb1f9c7f1c204630408
/usr/share/icons/Oxygen_Blue/cursors/6407b0e94181790501fd1e167b474872
/usr/share/icons/Oxygen_Blue/cursors/640fb0e74195791501fd1ed57b41487f
/usr/share/icons/Oxygen_Blue/cursors/9081237383d90e509aa00f00170e968f
/usr/share/icons/Oxygen_Blue/cursors/9d800788f1b08800ae810202380a0822
/usr/share/icons/Oxygen_Blue/cursors/X_cursor
/usr/share/icons/Oxygen_Blue/cursors/a2a266d0498c3104214a47bd64ab0fc8
/usr/share/icons/Oxygen_Blue/cursors/alias
/usr/share/icons/Oxygen_Blue/cursors/all-scroll
/usr/share/icons/Oxygen_Blue/cursors/b66166c04f8c3109214a4fbd64a50fc8
/usr/share/icons/Oxygen_Blue/cursors/circle
/usr/share/icons/Oxygen_Blue/cursors/closedhand
/usr/share/icons/Oxygen_Blue/cursors/col-resize
/usr/share/icons/Oxygen_Blue/cursors/color-picker
/usr/share/icons/Oxygen_Blue/cursors/copy
/usr/share/icons/Oxygen_Blue/cursors/cross
/usr/share/icons/Oxygen_Blue/cursors/crossed_circle
/usr/share/icons/Oxygen_Blue/cursors/d9ce0ab605698f320427677b458ad60b
/usr/share/icons/Oxygen_Blue/cursors/dnd-copy
/usr/share/icons/Oxygen_Blue/cursors/dnd-link
/usr/share/icons/Oxygen_Blue/cursors/dnd-move
/usr/share/icons/Oxygen_Blue/cursors/dnd-no-drop
/usr/share/icons/Oxygen_Blue/cursors/dnd-none
/usr/share/icons/Oxygen_Blue/cursors/e-resize
/usr/share/icons/Oxygen_Blue/cursors/e29285e634086352946a0e7090d73106
/usr/share/icons/Oxygen_Blue/cursors/fcf21c00b30f7e3f83fe0dfd12e71cff
/usr/share/icons/Oxygen_Blue/cursors/fleur
/usr/share/icons/Oxygen_Blue/cursors/forbidden
/usr/share/icons/Oxygen_Blue/cursors/half-busy
/usr/share/icons/Oxygen_Blue/cursors/hand1
/usr/share/icons/Oxygen_Blue/cursors/hand2
/usr/share/icons/Oxygen_Blue/cursors/help
/usr/share/icons/Oxygen_Blue/cursors/ibeam
/usr/share/icons/Oxygen_Blue/cursors/left_ptr
/usr/share/icons/Oxygen_Blue/cursors/left_ptr_watch
/usr/share/icons/Oxygen_Blue/cursors/link
/usr/share/icons/Oxygen_Blue/cursors/move
/usr/share/icons/Oxygen_Blue/cursors/n-resize
/usr/share/icons/Oxygen_Blue/cursors/ne-resize
/usr/share/icons/Oxygen_Blue/cursors/nesw-resize
/usr/share/icons/Oxygen_Blue/cursors/not-allowed
/usr/share/icons/Oxygen_Blue/cursors/nw-resize
/usr/share/icons/Oxygen_Blue/cursors/nwse-resize
/usr/share/icons/Oxygen_Blue/cursors/openhand
/usr/share/icons/Oxygen_Blue/cursors/pencil
/usr/share/icons/Oxygen_Blue/cursors/pirate
/usr/share/icons/Oxygen_Blue/cursors/plus
/usr/share/icons/Oxygen_Blue/cursors/pointer
/usr/share/icons/Oxygen_Blue/cursors/pointing_hand
/usr/share/icons/Oxygen_Blue/cursors/progress
/usr/share/icons/Oxygen_Blue/cursors/question_arrow
/usr/share/icons/Oxygen_Blue/cursors/row-resize
/usr/share/icons/Oxygen_Blue/cursors/s-resize
/usr/share/icons/Oxygen_Blue/cursors/sb_h_double_arrow
/usr/share/icons/Oxygen_Blue/cursors/sb_v_double_arrow
/usr/share/icons/Oxygen_Blue/cursors/se-resize
/usr/share/icons/Oxygen_Blue/cursors/size_all
/usr/share/icons/Oxygen_Blue/cursors/size_bdiag
/usr/share/icons/Oxygen_Blue/cursors/size_fdiag
/usr/share/icons/Oxygen_Blue/cursors/size_hor
/usr/share/icons/Oxygen_Blue/cursors/size_ver
/usr/share/icons/Oxygen_Blue/cursors/split_h
/usr/share/icons/Oxygen_Blue/cursors/split_v
/usr/share/icons/Oxygen_Blue/cursors/sw-resize
/usr/share/icons/Oxygen_Blue/cursors/text
/usr/share/icons/Oxygen_Blue/cursors/up_arrow
/usr/share/icons/Oxygen_Blue/cursors/v_double_arrow
/usr/share/icons/Oxygen_Blue/cursors/w-resize
/usr/share/icons/Oxygen_Blue/cursors/wait
/usr/share/icons/Oxygen_Blue/cursors/watch
/usr/share/icons/Oxygen_Blue/cursors/whats_this
/usr/share/icons/Oxygen_Blue/cursors/xterm
/usr/share/icons/Oxygen_Blue/index.theme
/usr/share/icons/Oxygen_White/cursors/00000000000000020006000e7e9ffc3f
/usr/share/icons/Oxygen_White/cursors/00008160000006810000408080010102
/usr/share/icons/Oxygen_White/cursors/03b6e0fcb3499374a867c041f52298f0
/usr/share/icons/Oxygen_White/cursors/08e8e1c95fe2fc01f976f1e063a24ccd
/usr/share/icons/Oxygen_White/cursors/1081e37283d90000800003c07f3ef6bf
/usr/share/icons/Oxygen_White/cursors/3085a0e285430894940527032f8b26df
/usr/share/icons/Oxygen_White/cursors/3ecb610c1bf2410f44200f48c40d3599
/usr/share/icons/Oxygen_White/cursors/4498f0e0c1937ffe01fd06f973665830
/usr/share/icons/Oxygen_White/cursors/5c6cd98b3f3ebcb1f9c7f1c204630408
/usr/share/icons/Oxygen_White/cursors/6407b0e94181790501fd1e167b474872
/usr/share/icons/Oxygen_White/cursors/640fb0e74195791501fd1ed57b41487f
/usr/share/icons/Oxygen_White/cursors/9081237383d90e509aa00f00170e968f
/usr/share/icons/Oxygen_White/cursors/9d800788f1b08800ae810202380a0822
/usr/share/icons/Oxygen_White/cursors/X_cursor
/usr/share/icons/Oxygen_White/cursors/a2a266d0498c3104214a47bd64ab0fc8
/usr/share/icons/Oxygen_White/cursors/alias
/usr/share/icons/Oxygen_White/cursors/all-scroll
/usr/share/icons/Oxygen_White/cursors/b66166c04f8c3109214a4fbd64a50fc8
/usr/share/icons/Oxygen_White/cursors/circle
/usr/share/icons/Oxygen_White/cursors/closedhand
/usr/share/icons/Oxygen_White/cursors/col-resize
/usr/share/icons/Oxygen_White/cursors/color-picker
/usr/share/icons/Oxygen_White/cursors/copy
/usr/share/icons/Oxygen_White/cursors/cross
/usr/share/icons/Oxygen_White/cursors/crossed_circle
/usr/share/icons/Oxygen_White/cursors/d9ce0ab605698f320427677b458ad60b
/usr/share/icons/Oxygen_White/cursors/dnd-copy
/usr/share/icons/Oxygen_White/cursors/dnd-link
/usr/share/icons/Oxygen_White/cursors/dnd-move
/usr/share/icons/Oxygen_White/cursors/dnd-no-drop
/usr/share/icons/Oxygen_White/cursors/dnd-none
/usr/share/icons/Oxygen_White/cursors/e-resize
/usr/share/icons/Oxygen_White/cursors/e29285e634086352946a0e7090d73106
/usr/share/icons/Oxygen_White/cursors/fcf21c00b30f7e3f83fe0dfd12e71cff
/usr/share/icons/Oxygen_White/cursors/fleur
/usr/share/icons/Oxygen_White/cursors/forbidden
/usr/share/icons/Oxygen_White/cursors/half-busy
/usr/share/icons/Oxygen_White/cursors/hand1
/usr/share/icons/Oxygen_White/cursors/hand2
/usr/share/icons/Oxygen_White/cursors/help
/usr/share/icons/Oxygen_White/cursors/ibeam
/usr/share/icons/Oxygen_White/cursors/left_ptr
/usr/share/icons/Oxygen_White/cursors/left_ptr_watch
/usr/share/icons/Oxygen_White/cursors/link
/usr/share/icons/Oxygen_White/cursors/move
/usr/share/icons/Oxygen_White/cursors/n-resize
/usr/share/icons/Oxygen_White/cursors/ne-resize
/usr/share/icons/Oxygen_White/cursors/nesw-resize
/usr/share/icons/Oxygen_White/cursors/not-allowed
/usr/share/icons/Oxygen_White/cursors/nw-resize
/usr/share/icons/Oxygen_White/cursors/nwse-resize
/usr/share/icons/Oxygen_White/cursors/openhand
/usr/share/icons/Oxygen_White/cursors/pencil
/usr/share/icons/Oxygen_White/cursors/pirate
/usr/share/icons/Oxygen_White/cursors/plus
/usr/share/icons/Oxygen_White/cursors/pointer
/usr/share/icons/Oxygen_White/cursors/pointing_hand
/usr/share/icons/Oxygen_White/cursors/progress
/usr/share/icons/Oxygen_White/cursors/question_arrow
/usr/share/icons/Oxygen_White/cursors/row-resize
/usr/share/icons/Oxygen_White/cursors/s-resize
/usr/share/icons/Oxygen_White/cursors/sb_h_double_arrow
/usr/share/icons/Oxygen_White/cursors/sb_v_double_arrow
/usr/share/icons/Oxygen_White/cursors/se-resize
/usr/share/icons/Oxygen_White/cursors/size_all
/usr/share/icons/Oxygen_White/cursors/size_bdiag
/usr/share/icons/Oxygen_White/cursors/size_fdiag
/usr/share/icons/Oxygen_White/cursors/size_hor
/usr/share/icons/Oxygen_White/cursors/size_ver
/usr/share/icons/Oxygen_White/cursors/split_h
/usr/share/icons/Oxygen_White/cursors/split_v
/usr/share/icons/Oxygen_White/cursors/sw-resize
/usr/share/icons/Oxygen_White/cursors/text
/usr/share/icons/Oxygen_White/cursors/up_arrow
/usr/share/icons/Oxygen_White/cursors/v_double_arrow
/usr/share/icons/Oxygen_White/cursors/w-resize
/usr/share/icons/Oxygen_White/cursors/wait
/usr/share/icons/Oxygen_White/cursors/watch
/usr/share/icons/Oxygen_White/cursors/whats_this
/usr/share/icons/Oxygen_White/cursors/xterm
/usr/share/icons/Oxygen_White/index.theme
/usr/share/icons/Oxygen_Yellow/cursors/00000000000000020006000e7e9ffc3f
/usr/share/icons/Oxygen_Yellow/cursors/00008160000006810000408080010102
/usr/share/icons/Oxygen_Yellow/cursors/03b6e0fcb3499374a867c041f52298f0
/usr/share/icons/Oxygen_Yellow/cursors/08e8e1c95fe2fc01f976f1e063a24ccd
/usr/share/icons/Oxygen_Yellow/cursors/1081e37283d90000800003c07f3ef6bf
/usr/share/icons/Oxygen_Yellow/cursors/3085a0e285430894940527032f8b26df
/usr/share/icons/Oxygen_Yellow/cursors/3ecb610c1bf2410f44200f48c40d3599
/usr/share/icons/Oxygen_Yellow/cursors/4498f0e0c1937ffe01fd06f973665830
/usr/share/icons/Oxygen_Yellow/cursors/5c6cd98b3f3ebcb1f9c7f1c204630408
/usr/share/icons/Oxygen_Yellow/cursors/6407b0e94181790501fd1e167b474872
/usr/share/icons/Oxygen_Yellow/cursors/640fb0e74195791501fd1ed57b41487f
/usr/share/icons/Oxygen_Yellow/cursors/9081237383d90e509aa00f00170e968f
/usr/share/icons/Oxygen_Yellow/cursors/9d800788f1b08800ae810202380a0822
/usr/share/icons/Oxygen_Yellow/cursors/X_cursor
/usr/share/icons/Oxygen_Yellow/cursors/a2a266d0498c3104214a47bd64ab0fc8
/usr/share/icons/Oxygen_Yellow/cursors/alias
/usr/share/icons/Oxygen_Yellow/cursors/all-scroll
/usr/share/icons/Oxygen_Yellow/cursors/b66166c04f8c3109214a4fbd64a50fc8
/usr/share/icons/Oxygen_Yellow/cursors/circle
/usr/share/icons/Oxygen_Yellow/cursors/closedhand
/usr/share/icons/Oxygen_Yellow/cursors/col-resize
/usr/share/icons/Oxygen_Yellow/cursors/color-picker
/usr/share/icons/Oxygen_Yellow/cursors/copy
/usr/share/icons/Oxygen_Yellow/cursors/cross
/usr/share/icons/Oxygen_Yellow/cursors/crossed_circle
/usr/share/icons/Oxygen_Yellow/cursors/d9ce0ab605698f320427677b458ad60b
/usr/share/icons/Oxygen_Yellow/cursors/dnd-copy
/usr/share/icons/Oxygen_Yellow/cursors/dnd-link
/usr/share/icons/Oxygen_Yellow/cursors/dnd-move
/usr/share/icons/Oxygen_Yellow/cursors/dnd-no-drop
/usr/share/icons/Oxygen_Yellow/cursors/dnd-none
/usr/share/icons/Oxygen_Yellow/cursors/e-resize
/usr/share/icons/Oxygen_Yellow/cursors/e29285e634086352946a0e7090d73106
/usr/share/icons/Oxygen_Yellow/cursors/fcf21c00b30f7e3f83fe0dfd12e71cff
/usr/share/icons/Oxygen_Yellow/cursors/fleur
/usr/share/icons/Oxygen_Yellow/cursors/forbidden
/usr/share/icons/Oxygen_Yellow/cursors/half-busy
/usr/share/icons/Oxygen_Yellow/cursors/hand1
/usr/share/icons/Oxygen_Yellow/cursors/hand2
/usr/share/icons/Oxygen_Yellow/cursors/help
/usr/share/icons/Oxygen_Yellow/cursors/ibeam
/usr/share/icons/Oxygen_Yellow/cursors/left_ptr
/usr/share/icons/Oxygen_Yellow/cursors/left_ptr_watch
/usr/share/icons/Oxygen_Yellow/cursors/link
/usr/share/icons/Oxygen_Yellow/cursors/move
/usr/share/icons/Oxygen_Yellow/cursors/n-resize
/usr/share/icons/Oxygen_Yellow/cursors/ne-resize
/usr/share/icons/Oxygen_Yellow/cursors/nesw-resize
/usr/share/icons/Oxygen_Yellow/cursors/not-allowed
/usr/share/icons/Oxygen_Yellow/cursors/nw-resize
/usr/share/icons/Oxygen_Yellow/cursors/nwse-resize
/usr/share/icons/Oxygen_Yellow/cursors/openhand
/usr/share/icons/Oxygen_Yellow/cursors/pencil
/usr/share/icons/Oxygen_Yellow/cursors/pirate
/usr/share/icons/Oxygen_Yellow/cursors/plus
/usr/share/icons/Oxygen_Yellow/cursors/pointer
/usr/share/icons/Oxygen_Yellow/cursors/pointing_hand
/usr/share/icons/Oxygen_Yellow/cursors/progress
/usr/share/icons/Oxygen_Yellow/cursors/question_arrow
/usr/share/icons/Oxygen_Yellow/cursors/row-resize
/usr/share/icons/Oxygen_Yellow/cursors/s-resize
/usr/share/icons/Oxygen_Yellow/cursors/sb_h_double_arrow
/usr/share/icons/Oxygen_Yellow/cursors/sb_v_double_arrow
/usr/share/icons/Oxygen_Yellow/cursors/se-resize
/usr/share/icons/Oxygen_Yellow/cursors/size_all
/usr/share/icons/Oxygen_Yellow/cursors/size_bdiag
/usr/share/icons/Oxygen_Yellow/cursors/size_fdiag
/usr/share/icons/Oxygen_Yellow/cursors/size_hor
/usr/share/icons/Oxygen_Yellow/cursors/size_ver
/usr/share/icons/Oxygen_Yellow/cursors/split_h
/usr/share/icons/Oxygen_Yellow/cursors/split_v
/usr/share/icons/Oxygen_Yellow/cursors/sw-resize
/usr/share/icons/Oxygen_Yellow/cursors/text
/usr/share/icons/Oxygen_Yellow/cursors/up_arrow
/usr/share/icons/Oxygen_Yellow/cursors/v_double_arrow
/usr/share/icons/Oxygen_Yellow/cursors/w-resize
/usr/share/icons/Oxygen_Yellow/cursors/wait
/usr/share/icons/Oxygen_Yellow/cursors/watch
/usr/share/icons/Oxygen_Yellow/cursors/whats_this
/usr/share/icons/Oxygen_Yellow/cursors/xterm
/usr/share/icons/Oxygen_Yellow/index.theme
/usr/share/icons/Oxygen_Zion/cursors/00000000000000020006000e7e9ffc3f
/usr/share/icons/Oxygen_Zion/cursors/00008160000006810000408080010102
/usr/share/icons/Oxygen_Zion/cursors/03b6e0fcb3499374a867c041f52298f0
/usr/share/icons/Oxygen_Zion/cursors/08e8e1c95fe2fc01f976f1e063a24ccd
/usr/share/icons/Oxygen_Zion/cursors/1081e37283d90000800003c07f3ef6bf
/usr/share/icons/Oxygen_Zion/cursors/3085a0e285430894940527032f8b26df
/usr/share/icons/Oxygen_Zion/cursors/3ecb610c1bf2410f44200f48c40d3599
/usr/share/icons/Oxygen_Zion/cursors/4498f0e0c1937ffe01fd06f973665830
/usr/share/icons/Oxygen_Zion/cursors/5c6cd98b3f3ebcb1f9c7f1c204630408
/usr/share/icons/Oxygen_Zion/cursors/6407b0e94181790501fd1e167b474872
/usr/share/icons/Oxygen_Zion/cursors/640fb0e74195791501fd1ed57b41487f
/usr/share/icons/Oxygen_Zion/cursors/9081237383d90e509aa00f00170e968f
/usr/share/icons/Oxygen_Zion/cursors/9d800788f1b08800ae810202380a0822
/usr/share/icons/Oxygen_Zion/cursors/X_cursor
/usr/share/icons/Oxygen_Zion/cursors/a2a266d0498c3104214a47bd64ab0fc8
/usr/share/icons/Oxygen_Zion/cursors/alias
/usr/share/icons/Oxygen_Zion/cursors/all-scroll
/usr/share/icons/Oxygen_Zion/cursors/b66166c04f8c3109214a4fbd64a50fc8
/usr/share/icons/Oxygen_Zion/cursors/circle
/usr/share/icons/Oxygen_Zion/cursors/closedhand
/usr/share/icons/Oxygen_Zion/cursors/col-resize
/usr/share/icons/Oxygen_Zion/cursors/color-picker
/usr/share/icons/Oxygen_Zion/cursors/copy
/usr/share/icons/Oxygen_Zion/cursors/cross
/usr/share/icons/Oxygen_Zion/cursors/crossed_circle
/usr/share/icons/Oxygen_Zion/cursors/d9ce0ab605698f320427677b458ad60b
/usr/share/icons/Oxygen_Zion/cursors/dnd-copy
/usr/share/icons/Oxygen_Zion/cursors/dnd-link
/usr/share/icons/Oxygen_Zion/cursors/dnd-move
/usr/share/icons/Oxygen_Zion/cursors/dnd-no-drop
/usr/share/icons/Oxygen_Zion/cursors/dnd-none
/usr/share/icons/Oxygen_Zion/cursors/e-resize
/usr/share/icons/Oxygen_Zion/cursors/e29285e634086352946a0e7090d73106
/usr/share/icons/Oxygen_Zion/cursors/fcf21c00b30f7e3f83fe0dfd12e71cff
/usr/share/icons/Oxygen_Zion/cursors/fleur
/usr/share/icons/Oxygen_Zion/cursors/forbidden
/usr/share/icons/Oxygen_Zion/cursors/half-busy
/usr/share/icons/Oxygen_Zion/cursors/hand1
/usr/share/icons/Oxygen_Zion/cursors/hand2
/usr/share/icons/Oxygen_Zion/cursors/help
/usr/share/icons/Oxygen_Zion/cursors/ibeam
/usr/share/icons/Oxygen_Zion/cursors/left_ptr
/usr/share/icons/Oxygen_Zion/cursors/left_ptr_watch
/usr/share/icons/Oxygen_Zion/cursors/link
/usr/share/icons/Oxygen_Zion/cursors/move
/usr/share/icons/Oxygen_Zion/cursors/n-resize
/usr/share/icons/Oxygen_Zion/cursors/ne-resize
/usr/share/icons/Oxygen_Zion/cursors/nesw-resize
/usr/share/icons/Oxygen_Zion/cursors/not-allowed
/usr/share/icons/Oxygen_Zion/cursors/nw-resize
/usr/share/icons/Oxygen_Zion/cursors/nwse-resize
/usr/share/icons/Oxygen_Zion/cursors/openhand
/usr/share/icons/Oxygen_Zion/cursors/pencil
/usr/share/icons/Oxygen_Zion/cursors/pirate
/usr/share/icons/Oxygen_Zion/cursors/plus
/usr/share/icons/Oxygen_Zion/cursors/pointer
/usr/share/icons/Oxygen_Zion/cursors/pointing_hand
/usr/share/icons/Oxygen_Zion/cursors/progress
/usr/share/icons/Oxygen_Zion/cursors/question_arrow
/usr/share/icons/Oxygen_Zion/cursors/row-resize
/usr/share/icons/Oxygen_Zion/cursors/s-resize
/usr/share/icons/Oxygen_Zion/cursors/sb_h_double_arrow
/usr/share/icons/Oxygen_Zion/cursors/sb_v_double_arrow
/usr/share/icons/Oxygen_Zion/cursors/se-resize
/usr/share/icons/Oxygen_Zion/cursors/size_all
/usr/share/icons/Oxygen_Zion/cursors/size_bdiag
/usr/share/icons/Oxygen_Zion/cursors/size_fdiag
/usr/share/icons/Oxygen_Zion/cursors/size_hor
/usr/share/icons/Oxygen_Zion/cursors/size_ver
/usr/share/icons/Oxygen_Zion/cursors/split_h
/usr/share/icons/Oxygen_Zion/cursors/split_v
/usr/share/icons/Oxygen_Zion/cursors/sw-resize
/usr/share/icons/Oxygen_Zion/cursors/text
/usr/share/icons/Oxygen_Zion/cursors/up_arrow
/usr/share/icons/Oxygen_Zion/cursors/v_double_arrow
/usr/share/icons/Oxygen_Zion/cursors/w-resize
/usr/share/icons/Oxygen_Zion/cursors/wait
/usr/share/icons/Oxygen_Zion/cursors/watch
/usr/share/icons/Oxygen_Zion/cursors/whats_this
/usr/share/icons/Oxygen_Zion/cursors/xterm
/usr/share/icons/Oxygen_Zion/index.theme
/usr/share/icons/hicolor/256x256/apps/oxygen-settings.png
/usr/share/kservices5/oxygendecorationconfig.desktop
/usr/share/kservices5/oxygenstyleconfig.desktop
/usr/share/kstyle/themes/oxygen.themerc
/usr/share/plasma/look-and-feel/org.kde.oxygen/contents/defaults
/usr/share/plasma/look-and-feel/org.kde.oxygen/contents/previews/preview.png
/usr/share/plasma/look-and-feel/org.kde.oxygen/contents/previews/splash.png
/usr/share/plasma/look-and-feel/org.kde.oxygen/contents/splash/Splash.qml
/usr/share/plasma/look-and-feel/org.kde.oxygen/contents/splash/images/background.png
/usr/share/plasma/look-and-feel/org.kde.oxygen/contents/splash/images/kde.png
/usr/share/plasma/look-and-feel/org.kde.oxygen/contents/splash/images/rectangle.png
/usr/share/plasma/look-and-feel/org.kde.oxygen/metadata.desktop

%files lib
%defattr(-,root,root,-)
/usr/lib64/liboxygenstyle5.so.5
/usr/lib64/liboxygenstyle5.so.5.26.5
/usr/lib64/liboxygenstyleconfig5.so.5
/usr/lib64/liboxygenstyleconfig5.so.5.26.5
/usr/lib64/qt5/plugins/kstyle_oxygen_config.so
/usr/lib64/qt5/plugins/org.kde.kdecoration2/oxygendecoration.so
/usr/lib64/qt5/plugins/styles/oxygen.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/oxygen/19d98e1b6f8ef12849ea4012a052d3907f336c91
/usr/share/package-licenses/oxygen/2123756e0b1fc8243547235a33c0fcabfe3b9a51
/usr/share/package-licenses/oxygen/3e8971c6c5f16674958913a94a36b1ea7a00ac46
/usr/share/package-licenses/oxygen/7d9831e05094ce723947d729c2a46a09d6e90275
/usr/share/package-licenses/oxygen/81b58c89ceef8e9f8bd5d00a287edbd15f9d3567
/usr/share/package-licenses/oxygen/81e12d0c07782abcf558af7aa19846e3e2606a70
/usr/share/package-licenses/oxygen/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/oxygen/a4c60b3fefda228cd7439d3565df043192fef137
/usr/share/package-licenses/oxygen/e3bdbf20d43fc066a1b40a64d57d4ae5a31f177f
/usr/share/package-licenses/oxygen/e458941548e0864907e654fa2e192844ae90fc32
/usr/share/package-licenses/oxygen/e7d563f52bf5295e6dba1d67ac23e9f6a160fab9

%files locales -f oxygen_style_config.lang -f oxygen_style_demo.lang -f liboxygenstyleconfig.lang -f oxygen_kdecoration.lang
%defattr(-,root,root,-)

