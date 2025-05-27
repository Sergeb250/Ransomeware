# 🔐 Educational Ransomware Simulation

> ⚠️ **DISCLAIMER:** This project is for **educational and ethical** purposes only. Do **not** use this script on any system without explicit permission. Misuse of this code may lead to **criminal charges**. The author assumes **no responsibility** for any damage caused.

## 📚 Overview

A simple Python script that encrypts and decrypts files in a folder using symmetric encryption (Fernet). Includes a secret passphrase check for decryption. Designed purely for educational purposes to demonstrate basic file encryption concepts.

![screenshot](https://github.com/Sergeb250/Ransomeware/blob/b42086301f761e151c330479e3c28bd5b0923c7d/Screenshot%202025-05-25%20202135.png)

---

## 📁 Project Structure

.
├── ransomware.py # Script to encrypt files

├── decrypt.py # Script to decrypt files with key + passphrase

├── thekey.key # Symmetric key (generated during encryption)

├── README.md # This file

yaml
Copy code



## ⚙️ Requirements

- Python 3.x  
- `cryptography` module

Install via pip:

```bash
pip install cryptography
```
🔒 How to Encrypt Files
⚠️ Warning: This will overwrite your files with encrypted versions.

```bash
Copy code
sudo python3 ransomware.py
```
🔓 How to Decrypt Files
```bash
Copy code
sudo python3 decrypt.py
```
Enter the secret passphrase amkiding when prompted.

Example: "amkiding"

🛡️ Ethical Usage
Use only in controlled environments and with permission. For educational and cybersecurity learning purposes only.

📜 License
MIT License — for educational use only. Not responsible for misuse.

✍️ Author

Igizeneza Serge Benit

Email: hacksergeb@gmail.com

Phone: 0791822315

