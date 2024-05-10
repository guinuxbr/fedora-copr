Name: kora-icon-theme
Version: 1.6.1
Release: 1%{?dist}
Summary: Kora is an SVG icon theme with lots of new icons for GNU/Linux operating systems.
License: GPL-3.0
URL: https://github.com/bikass/kora
Source0: %{url}/archive/refs/tags/v%{version}.tar.gz
BuildArch: noarch
BuildRequires: fdupes
Requires(post): gtk3

%description
Kora is an SVG icon theme with lots of new icons for GNU/Linux operating systems.

%prep
%setup -q -n kora-%{version}

%build
# Nothing to do here

%install
%fdupes %{buildroot}

# Delete useless files from source folder
rm -f "kora/create-new-icon-theme.cache.sh"
rm -f "kora/icon-theme.cache"
rm -f "kora-light/create-new-icon-theme.cache.sh"
rm -f "kora-light/icon-theme.cache"
rm -f "kora-light-panel/create-new-icon-theme.cache.sh"
rm -f "kora-light-panel/icon-theme.cache"
rm -f "kora-pgrey/create-new-icon-theme.cache.sh"
rm -f "kora-pgrey/icon-theme.cache"

# Install icons
mkdir -p %{buildroot}/usr/share/icons
cp -dr --no-preserve=mode "kora" %{buildroot}/usr/share/icons/kora
cp -dr --no-preserve=mode "kora-light" %{buildroot}/usr/share/icons/kora-light
cp -dr --no-preserve=mode "kora-light-panel" %{buildroot}/usr/share/icons/kora-light-panel
cp -dr --no-preserve=mode "kora-pgrey" %{buildroot}/usr/share/icons/kora-pgrey

# Install license
mkdir -p %{buildroot}/usr/share/licenses/%{name}
cp -p "LICENSE" %{buildroot}/usr/share/licenses/%{name}

%files
%doc README.md
%license LICENSE
/usr/share/icons/kora
/usr/share/icons/kora-light
/usr/share/icons/kora-light-panel
/usr/share/icons/kora-pgrey

%changelog
* Fri May 10 2024 GuinuxBR <guinuxbr@gmail.com> - 1.6.1
- Initial release