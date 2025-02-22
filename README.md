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

2. Run the installation script:

   ```bash
   bash BlueSky.sh --install
   ```
   or
   ```bash
   ./BlueSky.sh --install
   ```
   (Ensure the script is executable: `chmod +x BlueSky.sh`)

---

## Usage 🚀

### Interactive Mode:

To start an interactive search, use the following command:

```bash
bash BlueSky.sh --start
```

The tool will prompt you to enter a target (e.g., a phone number, email address, etc.) and perform the search across all supported data types.

---

### Direct Search:

You can search directly using one of the following options:

- **Search for a phone number**:
  ```bash
  bash BlueSky.sh --phones +1234567890
  ```
  or
  ```bash
  bash BlueSky.sh -p +1234567890
  ```

- **Search for a bank account**:
  ```bash
  bash BlueSky.sh --banks 1234567890123456
  ```
  or
  ```bash
  bash BlueSky.sh -b 1234567890123456
  ```

- **Search for an email address (Gmail)**:
  ```bash
  bash BlueSky.sh --email example@gmail.com
  ```
  or
  ```bash
  bash BlueSky.sh -e example@gmail.com
  ```

- **Search for an email address (Yahoo)**:
  ```bash
  bash BlueSky.sh --yaho example@yahoo.com
  ```
  or
  ```bash
  bash BlueSky.sh -y example@yahoo.com
  ```

- **Search for an Instagram username**:
  ```bash
  bash BlueSky.sh --insta username
  ```
  or
  ```bash
  bash BlueSky.sh -i username
  ```

- **Search for a TikTok username**:
  ```bash
  bash BlueSky.sh --tik username
  ```
  or
  ```bash
  bash BlueSky.sh -t username
  ```

- **Search for a name or username**:
  ```bash
  bash BlueSky.sh --name JohnDoe
  ```
  or
  ```bash
  bash BlueSky.sh -n JohnDoe
  ```

---

### Display Help Menu:

To display the help menu with a list of all options:

```bash
bash BlueSky.sh --help
```
or
```bash
bash BlueSky.sh -h
```

---

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
