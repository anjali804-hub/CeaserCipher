# Function to encrypt text using Caesar Cipher
def encrypt(text, shift):
    result = ""
    for i in range(len(text)):
        char = text[i]
        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char  # Keep non-alphabet characters unchanged
    return result

# Function to decrypt text using Caesar Cipher
def decrypt(text, shift):
    return encrypt(text, -shift)

# Main program
def main():
    print("Caesar Cipher Program")
    
    # Get user input
    choice = input("Do you want to encrypt or decrypt? (E/D): ").upper()
    if choice not in ['E', 'D']:
        print("Invalid choice. Please select 'E' for encryption or 'D' for decryption.")
        return

    message = input("Enter the message: ")
    shift = int(input("Enter the shift value: "))

    # Perform encryption or decryption
    if choice == 'E':
        encrypted_message = encrypt(message, shift)
        print("Encrypted message:", encrypted_message)
    elif choice == 'D':
        decrypted_message = decrypt(message, shift)
        print("Decrypted message:", decrypted_message)

if __name__ == "__main__":
    main()
