Name: nerd-fonts-hack
Version: 3.2.1
Release: 1%{?dist}
Summary: Nerd Fonts patched Hack font
License: MIT
Group: Fonts
URL: https://github.com/ryanoasis/nerd-fonts
Source0: %{url}/releases/download/v%{version}/Hack.tar.xz
BuildArch: noarch

%description
Nerd Fonts patched Hack font.

Nerd Fonts patches developer-focused fonts with a high number of glyphs (icons) from popular fonts like Font Awesome, Devicons, Octicons, etc.

%fontpkg -a

%prep
%setup -c -n %{name}-%{version}

%build
%fontbuild -a

%install
%fontinstall -a

%check
%fontcheck -a

%fontfiles -a

%changelog
* Fri May 10 2024 GuinuxBR <guinuxbr@gmail.com> - 3.2.1
- Initial release