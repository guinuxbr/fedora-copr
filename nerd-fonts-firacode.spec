Name: nerd-fonts-firacode
Version: 3.2.1
Release: 1%{?dist}
Summary: Nerd Fonts patched FiraCode font
License: MIT
Group: Fonts
URL: https://github.com/ryanoasis/nerd-fonts
Source0: %{url}/releases/download/v%{version}/FiraCode.tar.xz
BuildRoot: %{_tmppath}/%{name}-%{version}-build
BuildRequires: xz

%description
Nerd Fonts patched FiraCode font.

Nerd Fonts patches developer-focused fonts with a high number of glyphs (icons) from popular fonts like Font Awesome, Devicons, Octicons, etc.

%prep
%setup -q -n %{name}-%{version}

%build
# Nothing to do here (assumed unpacking happens during %setup)

%install
install -dm 0755 %{buildroot}%{_datadir}/fonts
install -Dm 0644 *.ttf %{buildroot}%{_datadir}/fonts/

%clean
[ "%{buildroot}" != "/" ] && %{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%dir %{_datadir}/fonts/
%{_datadir}/fonts/*

%post
if [ -x /usr/bin/fc-cache ]
then
    /usr/bin/fc-cache || :
fi

%postun
if [ $1 -eq 0 -a -x /usr/bin/fc-cache ]
then
    /usr/bin/fc-cache || :
fi

%changelog
* Fri May 10 2024 GuinuxBR <guinuxbr@gmail.com> - 3.2.1
- Initial release