Name: nerd-fonts-jetbrainsmono
Version: 3.4.0
Release: 1%{?dist}
Summary: Nerd Fonts patched JetBrainsMono font
License: MIT
Group: Fonts
URL: https://github.com/ryanoasis/nerd-fonts
Source0: %{url}/releases/download/v%{version}/JetBrainsMono.tar.xz
BuildArch: noarch

%define fontdir /usr/share/fonts/%{name}

%description
Nerd Fonts patched JetBrainsMono font.

Nerd Fonts patches developer-focused fonts with a high number of glyphs (icons) from popular fonts like Font Awesome, Devicons, Octicons, etc.

%fontpkg -a

%prep
%setup -c

%install
install -m 0644 -D -t %{buildroot}%{fontdir} *.ttf

%files
%{fontdir}/*.ttf
%license OFL.txt
%doc README.md

%changelog
* Mon Jun 22 2026 GuinuxBR <guinuxbr@gmail.com> - 3.4.0
- https://github.com/ryanoasis/nerd-fonts/releases/tag/v3.4.0
