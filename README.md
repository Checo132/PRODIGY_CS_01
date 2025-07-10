### caesar-cipher

#### 🛡️ CaesarX – A Beginner-Friendly Caesar Cipher Tool
---

This project is the implementation of a simple caesar cipher tool with python for encryting and decryting text, it is built with python, ran on a virtual machine, kali operating system to be precise. As a red teamer building this emphasises the red team mindset by demonstrating how to identify, simulate, and reverse weak encryption, while sharpening your scripting, cryptography, and offensive tooling skills.

---

#### ⚙️ Features

- Encrypt and decrypt messages using shift values
- Case-sensitive letter shifting
- Ignores symbols and spaces
- Run directly on Kali Linux or any UNIX system
- Easy-to-read code with comments



#### 🚀 How to Implement and use CaesarX Kali Linux

##### 1. Create a Project Folder and enter into the folder

mkdir caesar
cd caesar
---

##### 2. Create the Python File, save and exit.

vim caesar.py
Paste the following code (It shifts each letter in a message forward or backward in the alphabet by a number you choose, so the text becomes hidden (encrypted) or made readable again (decrypted)) within the file after triggering "insert" you could use nano for this also, I just prefer using vim;

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    print("=== CaesarX: Caesar Cipher Tool ===")
    choice = input("Encrypt or Decrypt? ").lower()
    message = input("Enter your message: ")
    try:
        shift = int(input("Enter shift value (0-25): "))
    except ValueError:
        print("Invalid shift. Please enter a number.")
        return

    if choice == 'encrypt':
        print("🔐 Encrypted:", encrypt(message, shift))
    elif choice == 'decrypt':
        print("🔓 Decrypted:", decrypt(message, shift))
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
---

##### 3. Run the python command to run the code within the caesar.py file

python3 caesar.py 
You get to see the option of encrypting snd decrypting, you insert your text, choose a number and it encrypts, run the command again, choose the number to decrypt;

=== Caesar Cipher Tool ===
Type 'encrypt' or 'decrypt': encrypt
Enter your message: Send me money
Enter the shift value (0-25): 20
🔐 Encrypted message: Myhx gy gihys

---
