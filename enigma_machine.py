
"""
A program that will encyrpt or decrypt a message using the Atbash Cipher technique
"""

import string
# Cipher technique used
def atbash_encrypt():
    message_input = input("Enter a message that you want to encyrpt: ").strip().upper()
    ciphertext = ""
    for letter in message_input:
        ascii = ord(letter)
        if ascii>=65 and ascii<=90:
            position = ascii - 65
            newPosition = 25 - position
            newAscii = newPosition + 65
            newLetter = chr(newAscii)
        else:
            newLetter = letter
        ciphertext = ciphertext + newLetter

    print(f"\nYour message: {message_input}")
    print("The encrypted message is:")
    print(ciphertext)

def atbash_decrypt():
    message_input = input("Enter a message that you want to decrypt: ").strip().upper()
    ciphertext = ""
    for letter in message_input:
        ascii = ord(letter)
        if ascii>=65 and ascii<=90:
            position = ascii - 65
            newPosition = 25 - position
            newAscii = newPosition + 65
            newLetter = chr(newAscii)
        else:
            newLetter = letter
        ciphertext = ciphertext + newLetter

    print(f"\nYour message: {message_input}")
    print("The encrypted message is:")
    print(ciphertext)


# Greet the user and explain them what this program does
print("Hey user!")
print("Welcome to the Atbash Cipher enigma machine!")
print("This program will either encrypt or decrypt a message in the Atbash Cipher")
print("Let's get started!")

# Ask the user whether they want to decrypt or encrypt a message
while True:
    ask = input(f"\nDo you want to encrypt or decrypt a message?: [e/d]:  ").lower().strip()
    if ask in ['e', 'd']:
        break
    else:
        print("Invalid! Enter either [e]ncrypt or [d]ecrypt.")
        continue

if ask == "e":
    atbash_encrypt()

elif ask == "d":
    atbash_decrypt()



# Create two functions that will encrypt and decrypt messages 


# Present the final encrypted or decrypted message to user


# Ask if they want to do another encryption or decryption


# Goodbye