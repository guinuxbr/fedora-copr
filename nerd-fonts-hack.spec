Name: nerd-fonts-hack
Version: 3.3.0
Release: 1%{?dist}
Summary: Nerd Fonts patched Hack font
License: MIT
Group: Fonts
URL: https://github.com/ryanoasis/nerd-fonts
Source0: %{url}/releases/download/v%{version}/Hack.tar.xz
BuildArch: noarch

%define fontdir /usr/share/fonts/%{name}

%description
Nerd Fonts patched Hack font.

Nerd Fonts patches developer-focused fonts with a high number of glyphs (icons) from popular fonts like Font Awesome, Devicons, Octicons, etc.

%fontpkg -a

%prep
%setup -c

%install
install -m 0644 -D -t %{buildroot}%{fontdir} *.ttf

%files
%{fontdir}/*.ttf
%license LICENSE.md
%doc README.md

%changelog
* Tue Dec 03 2024 GuinuxBR <guinuxbr@gmail.com> - 3.3.0
- https://github.com/ryanoasis/nerd-fonts/releases/tag/v3.3.0

* Sat May 11 2024 GuinuxBR <guinuxbr@gmail.com> - 3.2.1
- Initial release