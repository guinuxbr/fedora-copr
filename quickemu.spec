%global debug_package %{nil}
Name: quickemu
Version: 4.9.4
Release: 1%{?dist}
Summary: Quickly create and run optimised Windows, macOS and Linux desktop virtual machines
License: MIT
Group: Applications/Emulators
URL: https://github.com/quickemu-project/quickemu
Source0: %{url}/archive/refs/tags/%{version}.tar.gz
Requires: qemu bash coreutils edk2-tools grep jq mesa-demos pciutils procps python3 genisoimage usbutils util-linux sed socat spice-gtk-tools swtpm xdg-user-dirs xrandr unzip

%description
Quickly create and run optimised Windows, macOS and Linux desktop virtual machines.

%prep
%setup -q

%build

%install
install -Dm644 LICENSE %{buildroot}/%{_licensedir}/%{name}/LICENSE
install -Dm755 quickemu %{buildroot}/%{_bindir}/quickemu
install -Dm755 chunkcheck %{buildroot}/%{_bindir}/chunkcheck
install -Dm755 quickget %{buildroot}/%{_bindir}/quickget

install -Dm644 docs/quickget.1 %{buildroot}/%{_mandir}/man1/quickget.1
install -Dm644 docs/quickemu.1 %{buildroot}/%{_mandir}/man1/quickemu.1
install -Dm644 docs/quickemu_conf.1 %{buildroot}/%{_mandir}/man1/quickemu_conf.1

%files
%{_bindir}/quickemu
%{_bindir}/chunkcheck
%{_bindir}/quickget
%{_licensedir}/%{name}/LICENSE
%{_mandir}/man1/

%changelog
* Sat May 11 2024 GuinuxBR <guinuxbr@gmail.com> - 4.9.4
- Initial release
