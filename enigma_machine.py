
"""
A program that will encyrpt or decrypt a message using the Atbash Cipher technique
"""

import string
# Cipher technique used
def atbash(s):
    new_string = ""
    lower_case = string.ascii_lowercase[0:]
    reverse_string = lower_case[::-1]
    for i in s:
        if i == "" or i == "." or i == ",":
            new_string+=i
        elif i.isdigit():
            new_string+=i
        elif i in ["$", "^", "!", "*", "'", '"']:
            new_string+=i
    for j in range(len(lower_case)):
        if i == lower_case[j] or i == lower_case[j].upper():
            if i == i.upper():
                i = reverse_string[j].upper()
                new_string+=i
            else:
                i = reverse_string[j]
                new_string+=i
            break

    text_input = input("Enter any text you want:  ")
    text= "'''" + text_input + "'''"
    for x in text.split(" "):
        mirror_text = atbash(x)
        cipher_text = mirror_text.replace("'''", "")
        print(cipher_text, end = " ")
        return new_string



# Greet the user and explain them what this program does
print("Hey user!")
print("Welcome to the Atbash Cipher enigma machine!")
print("This program will either encrypt or decrypt a message in the Atbash Cipher")
print(f"Let's get started!\n")

# Ask the user whether they want to decrypt or encrypt a message
while True:
    ask = input(f"Do you want to encrypt or decrypt a message?: [e/d]:  \n").lower().strip()
    if ask in ['e', 'd']:
        break
    else:
        print("Invalid! Enter either [e]ncrypt or [d]ecrypt.")
        continue

if ask == "e":
    atbash(s)



# Create two functions that will encrypt and decrypt messages 


# Present the final encrypted or decrypted message to user


# Ask if they want to do another encryption or decryption


# Goodbye