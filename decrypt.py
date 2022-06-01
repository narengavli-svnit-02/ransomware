#importing file
import os
from cryptography.fernet import Fernet

#fetch all file and add in files list
files=[]
for file in os.listdir():
    if file == "voldermort.py" or file == "thekey.key" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)

#fetch key from file
with open("thekey.key","rb") as key:
    secret_key = key.read()

#decrypt date
for file in files:
    with open(file,"rb") as thefile:
        contents = thefile.read()
    contents_decrypted = Fernet(secret_key).decrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_decrypted)
