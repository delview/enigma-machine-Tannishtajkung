
"""
A program that will encyrpt or decrypt a message using the Atbash Cipher technique
"""
# Atbash dictionary from A to Z
atbash_dict = {
    'A': 'Z',
    'B': 'Y',
    'C': 'X',
    'D': 'W',
    'E': 'V',
    'F': 'U',
    'G': 'T',
    'H': 'S',
    'I': 'R',
    'J': 'Q',
    'K': 'P',
    'L': 'O',
    'M': 'N',
    'N': 'M',
    'O': 'L',
    'P': 'K',
    'Q': 'J',
    'R': 'I',
    'S': 'H',
    'T': 'G',
    'U': 'F',
    'V': 'E',
    'W': 'D',
    'X': 'C',
    'Y': 'B',
    'Z': 'A'
}

def atbash_cipher(): # Function that encrypts or decrypt the message
    result = ""
    message_input = input("Enter your message: ").strip().upper()
    for letter in message_input:
        if letter in atbash_dict:
            result += atbash_dict[letter] # Replace using the dictionary
        else:
            result += letter
 
    print(f"\nThe message you entered:") # The original message
    print(f"{message_input}")
    print(f"\nThe decrypted message is:") # The new message
    print(result)
    print("")
    return
   

def help_cipher(): # Will explain the user what the Atbash Cipher is 
    print(f"\nThe Atbash Cipher is a very old Substitution Cipher that was originally developed for use with the Hebrew alphabet.")
    print("In fact, in the Book of Jeremiah there are several words that have been enciphered using the Atbash Cipher.")
    print("It is generally considered one of the easiest ciphers to use as it follows a very simple substitution method.")
    print("The first letter of the alphabet is replaced with the last letter, the second letter is replaced with the second from last, and so on.")
    print("So the first letter (A) becomes the last letter (Z), and the second letter (B) becomes the second to last letter (Y), and so on.")
    print("")
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

    # Call atbash_cipher function
    atbash_cipher()

    # Ask if they want to do another encryption or decryption
    while True:
        choice = input("Do you want to do another encryption and decryption? [y/n]:  ").lower().strip()
        if choice in ['y', 'n']:
            break
        else:
            print(f"Invalid! Enter either [y]es or [n]o.\n")
            continue

    if choice == "n": # Will take the user to the goodbye message
        break

    if choice == "y": # Will loop through the code again
        print(f"YEAH! Let's do this!.\n")

# Goodbye
print("Thanks for using the Atbash Cipher enigma machine. See you soon!")
print("")