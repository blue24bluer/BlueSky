---

# BlueSky 🌌

BlueSky is a powerful **Bash script** designed to search for information across multiple online databases. It supports searching for phone numbers, bank account details, email addresses, usernames, and more. The tool is intended to be simple and straightforward for quickly gathering publicly available information.

---

## Key Features 🌟

- **Multi-Database Search**: Searches across various online databases for specified targets.
- **Data Type Support**: Supports searching for:
  - Phone numbers 📞
  - Bank account details 💳
  - Email addresses (Gmail, Yahoo) 📧
  - Instagram usernames 📸
  - TikTok usernames 🎵
  - Names or usernames 👤
- **Colorized Output**: Provides a visually appealing and informative output using ANSI color codes.
- **Dependency Check**: Verifies the presence of necessary utilities like `curl` and `grep`.
- **Easy Installation**: Includes a simple installation process.
- **Comprehensive Help Menu**: Offers detailed usage instructions.
- **Network Check**: Verifies internet connectivity before performing searches.
- **Termux Compatibility**: Works seamlessly with the Termux app on Android.
- **Anti-Piracy System**: Ensures the tool is downloaded legally.

---

## Dependencies ⚙️

To run BlueSky, ensure the following tools are installed:

- `bash`
- `curl`
- `grep`
- `wget` (for network checks)
- `ifconfig` or `ip` (for IP address retrieval)
- `apt` or a similar package manager (for installation)

---

## Installation 📥

1. Clone the repository:

   ```bash
   git clone https://github.com/blue24bluer/BlueSky
   cd BlueSky
   ```

2. Run the web server:

   ```bash
   python bluesky_main.py
   ```

BlueSky-GUI is the graphical user interface of the BlueSky project, designed to provide users with an intuitive and accessible way to interact with the system.

### Interface Preview

<div align="center">
  <img
    src="https://i.postimg.cc/2Szm58wB/Screenshot-2026-10-05-004412.png"
    alt="BlueSky-GUI Interface Preview"
    width="900"
  />
  <p><em>BlueSky-GUI — Graphical User Interface</em></p>
</div>

### Overview

BlueSky-GUI provides a visual interface for interacting with BlueSky, making its functionality accessible through a graphical environment rather than relying exclusively on command-line interaction.

---
 
   (Ensure the script is executable: `chmod +x bluesky_main.py`)

---

2. Run the terminal tool:

    ```bash
    python Libs/Tools/BlueSky.py
    ```
---

## Usage 🚀
```
┌──────────────────────────────────────────────────────────────────────┐
│                                                                      │
│ ▄▄▄▄▄▄    ▄▄▄▄                            ▄▄▄▄    ▄▄                 │
│ ██▀▀▀▀██  ▀▀██                          ▄█▀▀▀▀█   ██                 │
│ ██    ██    ██      ██    ██   ▄████▄   ██▄       ██ ▄██▀   ▀██  ███ │
│ ███████     ██      ██    ██  ██▄▄▄▄██   ▀████▄   ██▄██      ██▄ ██  │
│ ██    ██    ██      ██    ██  ██▀▀▀▀▀▀       ▀██  ██▀██▄      ████▀  │
│ ██▄▄▄▄██    ██▄▄▄   ██▄▄▄███  ▀██▄▄▄▄█  █▄▄▄▄▄█▀  ██  ▀█▄      ███   │
│ ▀▀▀▀▀▀▀      ▀▀▀▀    ▀▀▀▀ ▀▀    ▀▀▀▀▀    ▀▀▀▀▀    ▀▀   ▀▀▀     ██    │
│                                                              ███     │
│@$blue24bluer                                                          │
└──────────────────────────────────────────────────────────────────────┘
```

.1 FOR HELP :
```
┌─[root@parrot]─[~/DEV/BlueSky/Libs/Tools]
└──╼ #python BlueSky.py -h
usage: BlueSky.py [-h] [-s <term>] [-i]

USAGE OF BlueSkay: Search for data.

options:
  -h, --help            show this help message and exit
  -s <term>, --search <term>
                        Search for a term (phone, email, name, etc.).
  -i, --install         Show instructions to install required tools.
┌─[root@parrot]─[~/DEV/BlueSky/Libs/Tools]
└──╼ #
```

.2 FOR START INSTALLION

```
┌─[root@parrot]─[~/DEV/BlueSky/Libs/Tools]
└──╼ #python BlueSky.py -i
```

## Contributing 🤝

Contributions are welcome! Feel free to submit pull requests or open issues to suggest improvements or report bugs.

---

## License 📜

This project is licensed under the **MIT License**. For more details, see the [LICENSE](LICENSE) file.

---

## Disclaimer ⚠️

This tool is intended for **educational and research purposes only**. The author is not responsible for any misuse of this tool. Always respect privacy and adhere to applicable laws and regulations.

---

## Contact the Developer 📞

For any questions, issues, or support, you can contact the developer via:

- **Facebook**: [Profile](https://www.facebook.com/profile.php?id=100091250776579&mibextid=ZbWKwL)
- **WhatsApp**: +*** *** *** ***
- **Instagram**: [@_blue24bluer_](https://instagram.com/_blue24bluer_)
- **Telegram**: [@blue24bluer](https://t.me/blue24bluer)
- **TikTok**: [@_blue24bluer_](https://tiktok.com/@_blue24bluer_)
- **Reddit**: [Profile](https://www.reddit.com/u/Blue24Bluer/s/CUClygKPHV)
- **Twitter**: [@Blue24Bluer](https://twitter.com/Blue24Bluer)

---

This `README.md` provides a comprehensive guide to the tool, including installation instructions, usage examples, and contact information for support. It’s designed to be user-friendly and informative for both beginners and advanced users.
