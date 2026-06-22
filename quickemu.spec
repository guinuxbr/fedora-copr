%global debug_package %{nil}
Name: quickemu
Version: 4.9.9
Release: 1%{?dist}
Summary: Quickly create and run optimised Windows, macOS and Linux desktop virtual machines
License: MIT
Group: Applications/Emulators
URL: https://github.com/quickemu-project/quickemu
Source0: %{url}/archive/refs/tags/%{version}.tar.gz
BuildRequires: make
Requires: qemu bash coreutils edk2-tools grep jq mesa-demos pciutils procps python3 genisoimage usbutils util-linux sed socat spice-gtk-tools swtpm xdg-user-dirs xrandr unzip

%description
Quickly create and run optimised Windows, macOS and Linux desktop virtual machines.

%prep
%setup -q

%build

%install
# Install the scripts and manpages
%make_install -C docs mandir=%{_mandir} bindir=%{_bindir}

%files
%license LICENSE
%doc README.md
%{_bindir}/chunkcheck
%{_bindir}/quickemu
%{_bindir}/quickget
%{_bindir}/quickreport
%{_mandir}/man1/quickemu.1*
%{_mandir}/man5/quickemu_conf.5*
%{_mandir}/man1/quickget.1*

%changelog
* Mon Jun 22 2026 GuinuxBR <guinuxbr@gmail.com> - 4.9.9
- https://github.com/quickemu-project/quickemu/releases/tag/4.9.9

* Mon May 26 2025 GuinuxBR <guinuxbr@gmail.com> - 4.9.7
- https://github.com/quickemu-project/quickemu/releases/tag/4.9.7

* Mon Aug 26 2024 GuinuxBR <guinuxbr@gmail.com> - 4.9.6
- Added more comprehensive testing in CI 🧪
- Added all required documents/policies to complete Community Standards ⭐️
- Updated Nix flake to track current stable Nixpkgs for builds ❄️
- Fixed Nix flake so the build-in QEMU smb server works 📂
- Fixed kill running virtual machines with --kill ☠️
- Fixed Windows Server having no network post-install 🪟
- Fixed Fedora Silverblue downloads 💿️
- Improve automatic "press any key" for Windows installs 🪟
- Dropped Windows 8.1, Windows 10 LTSC and Windows Server 2012 R2 🪟
- Dropped ncurses dependency 🖥️

* Sat May 11 2024 GuinuxBR <guinuxbr@gmail.com> - 4.9.4
- Initial release
