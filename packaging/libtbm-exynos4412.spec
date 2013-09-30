Name:           libtbm-exynos4412
Version:        1.0.4
Release:        6
License:        MIT
Summary:        Tizen Buffer Manager - exynos4412 backend
Group:          System/Libraries
ExcludeArch:    i586
Source0:        %{name}-%{version}.tar.gz

%description
descriptionion: ${summary}

%prep
%setup -q

%build

autoreconf -vfi
./configure --prefix=%{_prefix} --libdir=%{_libdir}/bufmgr

make %{?jobs:-j%jobs}

%install
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
/usr/share/license/%{name}
%{_libdir}/bufmgr/libtbm_*.so*

