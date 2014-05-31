Name:           libtbm-exynos4412
Version:        1.0.5
Release:        1
License:        MIT
Summary:        Tizen Buffer Manager - exynos4412 backend
Group:          System/Libraries
ExcludeArch:    i586
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  pkgconfig(pthread-stubs)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libtbm)

Requires:   libtbm
Requires:   libdrm2

%description
descriptionion: ${summary}

%prep
%setup -q

%build

%reconfigure --prefix=%{_prefix} --libdir=%{_libdir}/bufmgr \
            CFLAGS="${CFLAGS} -Wall -Werror" LDFLAGS="${LDFLAGS} -Wl,--hash-style=both -Wl,--as-needed"

make %{?_smp_mflags}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/license
cp -af COPYING %{buildroot}/usr/share/license/%{name}
%make_install


%post
if [ -f %{_libdir}/bufmgr/libtbm_default.so ]; then
    rm -rf %{_libdir}/bufmgr/libtbm_default.so
fi
ln -s libtbm_exynos4412.so %{_libdir}/bufmgr/libtbm_default.so

%postun -p /sbin/ldconfig

%files
%{_libdir}/bufmgr/libtbm_*.so*
/usr/share/license/%{name}

