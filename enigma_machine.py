
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

    print(f"\nThe message you entered:")
    print(f"{message_input}")
    print(f"\nThe encrypted message is:")
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

    print(f"\nThe message you entered:")
    print(f"{message_input}")
    print("The decrypted message is:")
    print(ciphertext)
    print("")
    return

def help(): # Will explain the user what the Atbash Cipher is 
    print("")



# Greet the user and explain them what this program does
print(f"\nHey user!")
print("Welcome to the Atbash Cipher enigma machine!")
print("This program will either encrypt or decrypt a message in the Atbash Cipher.")
print("Don't know what an Atbash Cipher is?")
while True:  
    help = input("[Press H] for a detailed explanation or [Press X] if you already know:  ").title().strip()
    if help in ['H', 'X']:
        break
    else:
        print("Invalid! Enter either [H]elp or [X] to cancel.")
        continue

if help == "H":
    help()
    
if help == "X":
    print("Let's get started!")

while True:
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


    # Ask if they want to do another encryption or decryption
    while True:
        choice = input("Do you want to do another encryption and decryption? [y/n]:  ").lower().strip()
        if choice in ['y', 'n']:
            break
        else:
            print("Invalid! Enter either [y]es or [n]o.")
            continue

    if choice == "n":
        break

    if choice == "y":
        print("YEAH! Let's do another encryption/ decryption of a message.")

# Goodbye
print("Thanks for using the Atbash Cipher enigma machine. See you soon!")