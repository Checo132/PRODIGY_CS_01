def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted_char = (ord(char) - base + shift) % 26 + base
            result += chr(shifted_char)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

message = input("Hello, World!: ") 
shift = int(input("3: ")) 
encrypted = caesar_encrypt(message, shift)
decrypted = caesar_decrypt(encrypted, shift)

print("Encrypted:", encrypted)
print("Decrypted:", decrypted)

try:
    shift = int(input("Enter shift value: "))
except ValueError:
    print("Please enter a valid number for the shift.")
    exit()

mode = input("Type 'encrypt' or 'decrypt': ").lower()


