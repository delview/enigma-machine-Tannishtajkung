
"""
A program that will encyrpt or decrypt a message using the Atbash Cipher technique
"""

# Cipher technique used
def atbash_encrypt(): # Function that encrypts the message
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

    print(f"\nThe message you entered:") # The original message
    print(f"{message_input}")
    print(f"\nThe encrypted message is:") # The new message
    print(ciphertext)
    print("")
    return

def atbash_decrypt(): # Function that decrypt the message
    message_input = input("Enter a message that you want to decrypt: ").strip().upper()
    ciphertext = ""
    for letter in message_input:
        ascii = ord(letter)
        if ascii>=90 and ascii<=65:
            position = ascii - 90
            newPosition = -25 - position
            newAscii = newPosition + 90
            newLetter = chr(newAscii)
        else:
            newLetter = letter
        ciphertext = ciphertext + newLetter

    print(f"\nThe message you entered:") # The original message
    print(f"{message_input}")
    print("The decrypted message is:") # The new message
    print(ciphertext)
    print("")
    return

def help_cipher(): # Will explain the user what the Atbash Cipher is 
    print(f"\nThe Atbash Cipher is a very old Substitution Cipher that was originally developed for use with the Hebrew alphabet.")
    print("In fact, in the Book of Jeremiah there are several words that have been enciphered using the Atbash Cipher.")
    print("It is generally considered one of the easiest ciphers to use as it follows a very simple substitution method.")
    print("The first letter of the alphabet is replaced with the last letter, the second letter is replaced with the second from last, and so on.")
    print("So the first letter (A) becomes the last letter (Z), and the second letter (B) becomes the second to last letter (Y), and so on.")
    return

# Greet the user and explain them what this program does
print(f"\nHey user!")
print("Welcome to the Atbash Cipher enigma machine!")
print("This program will either encrypt or decrypt a message in the Atbash Cipher.")
print(f"\nDon't know what an Atbash Cipher is?")
while True:  
    help = input("[Press h] for a detailed explanation or [Press x] if you already know:  ").lower().strip() # Ask if they need help 
    if help in ['h', 'x']:
        break
    else:
        print(f"Invalid! Enter either [h]elp or [x] to cancel.\n")
        continue

if help == "h":
    help_cipher() # Will call the function that explains the user what the Atbash Cipher does
    
if help == "x":
    print(f"Let's get started!\n")

while True:
    # Ask the user whether they want to decrypt or encrypt a message
    while True:
        ask = input(f"Do you want to encrypt or decrypt a message?: [e/d]:  ").lower().strip()
        if ask in ['e', 'd']:
            break
        else:
            print(f"Invalid! Enter either [e]ncrypt or [d]ecrypt.\n")
            continue

    if ask == "e":
        atbash_encrypt() # Will call the encrypt function

    elif ask == "d":
        atbash_decrypt() # Will call the decrypt function


    # Ask if they want to do another encryption or decryption
    while True:
        choice = input("Do you want to do another encryption and decryption? [y/n]:  ").lower().strip()
        if choice in ['y', 'n']:
            break
        else:
            print(f"Invalid! Enter either [y]es or [n]o.\n")
            continue

    if choice == "n":
        break

    if choice == "y":
        print("YEAH! Let's do another encryption/ decryption of a message.")

# Goodbye
print("Thanks for using the Atbash Cipher enigma machine. See you soon!")
print("")