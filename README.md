# Fedora Copr Repository

[![Fedora Copr][copr-shield]][copr-url]
[![Build Status][builds-shield]][builds-url]
[![Issues][issues-shield]][issues-url]

Personal repository to manage RPM packages built using [Fedora Copr](https://copr.fedoraproject.org/) for Fedora
systems.

---

## 🚀 Quick Start

To enable this repository and install packages:

Enable the Copr repository:

```bash
sudo dnf copr enable guinuxbr/fedora-copr
```

Install a package:

```bash
sudo dnf install <package-name>
```

---

## 📦 Available Packages

| Package                        | Description                                                     | Upstream                                                                  | Status                     |
| :----------------------------- | :-------------------------------------------------------------- | :------------------------------------------------------------------------ | :------------------------- |
| **`kora-icon-theme`**          | SVG icon theme with lots of new icons for GNU/Linux             | [bikass/kora](https://github.com/bikass/kora)                             | Active                     |
| **`nerd-fonts-firacode`**      | Iconic font aggregator, collection, & patcher                   | [ryanoasis/nerd-fonts](https://github.com/ryanoasis/nerd-fonts)           | Active                     |
| **`nerd-fonts-hack`**          | Iconic font aggregator, collection, & patcher                   | [ryanoasis/nerd-fonts](https://github.com/ryanoasis/nerd-fonts)           | Active                     |
| **`nerd-fonts-jetbrainsmono`** | Iconic font aggregator, collection, & patcher                   | [ryanoasis/nerd-fonts](https://github.com/ryanoasis/nerd-fonts)           | Active                     |
| **`starship`**                 | Minimal, blazing-fast, and infinitely customizable shell prompt | [starship/starship](https://github.com/starship/starship)                 | Active                     |
| ~~`quickemu`~~                 | Quickly create and run optimized Windows, macOS, and Linux VMs  | [quickemu-project/quickemu](https://github.com/quickemu-project/quickemu) | *In official Fedora repos* |

---

## 🛠️ Build Status & Contributions

You can check the build status for each package on [Fedora Copr Builds][builds-url].

If you would like to contribute or request a specific package, please [open an issue][issues-url].

[copr-shield]: https://img.shields.io/badge/Fedora%20Copr-guinuxbr%2Ffedora--copr-blue?style=flat-square&logo=fedora
[copr-url]: https://copr.fedorainfracloud.org/coprs/guinuxbr/fedora-copr/
[builds-shield]: https://img.shields.io/badge/Builds-Fedora%20Copr-5254cf?style=flat-square&logo=fedora
[builds-url]: https://copr.fedorainfracloud.org/coprs/guinuxbr/fedora-copr/builds/
[issues-shield]: https://img.shields.io/github/issues/guinuxbr/fedora-copr?style=flat-square
[issues-url]: https://github.com/guinuxbr/fedora-copr/issues
