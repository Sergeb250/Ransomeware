import os
from cryptography.fernet import Fernet, InvalidToken

phrase = input("Enter the secret phrase: ")
if phrase != "amkiding":
    print("Wrong phrase.")
    exit()

if not os.path.exists("thekey.key"):
    print("Key file not found.")
    exit()

files = []
for file in os.listdir():
    if file in ["ransomeware.py", "thekey.key", "decrypt.py"]:
        continue
    if os.path.isfile(file):
        files.append(file)

with open("thekey.key", "rb") as key_file:
    secret_key = key_file.read()

for file in files:
    try:
        with open(file, "rb") as f:
            contents = f.read()
        contents_decrypted = Fernet(secret_key).decrypt(contents)
        with open(file, "wb") as f:
            f.write(contents_decrypted)
        print(f"Decrypted {file}")
    except InvalidToken:
        print(f"Invalid key or not an encrypted file: {file}")
    except Exception as e:
        print(f"Failed to decrypt {file}: {e}")
