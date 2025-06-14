%global debug_package %{nil}
%undefine _package_note_file
Name: starship
Version: 1.23.0
Release: 1%{?dist}
Summary: Minimal, blazing-fast, and infinitely customizable prompt for any shell!
License: ISC
URL: https://github.com/starship/starship
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires: cargo >= 1.74
BuildRequires: cmake3
BuildRequires: gcc
BuildRequires: rust >= 1.74
BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(zlib)

%description
Minimal, blazing-fast, and infinitely customizable prompt for any shell!

%prep
%autosetup

%install
export CARGO_PROFILE_RELEASE_BUILD_OVERRIDE_OPT_LEVEL=3
export CMAKE=cmake3
RUSTFLAGS='-C strip=symbols' cargo install --root=%{buildroot}%{_prefix} --path=.
rm -f %{buildroot}%{_prefix}/.crates.toml \
    %{buildroot}%{_prefix}/.crates2.json

%files
%license LICENSE
%doc README.md CONTRIBUTING.md
%{_bindir}/%{name}

%changelog
* Mon May 26 2025 GuinuxBR <guinuxbr@gmail.com> - 1.23.0
- https://github.com/starship/starship/releases/tag/v1.23.0

* Tue Dec 03 2024 GuinuxBR <guinuxbr@gmail.com> - 1.21.1
- https://github.com/starship/starship/releases/tag/v1.21.1

* Mon Aug 26 2024 GuinuxBR <guinuxbr@gmail.com> - 1.20.1
- Bug Fixes
    - ci: move to macos-latest image (#6132) (c7a8ea7)

* Fri May 10 2024 GuinuxBR <guinuxbr@gmail.com> - 1.18.2
- Initial release
