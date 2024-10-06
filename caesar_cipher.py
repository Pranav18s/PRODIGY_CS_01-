def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.isupper():
                encrypted_text += chr((ord(char) + shift_amount - 65) % 26 + 65)
            else:
                encrypted_text += chr((ord(char) + shift_amount - 97) % 26 + 97)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    while True:
        print("Caesar Cipher Program")
        mode = input("Would you like to (E)ncrypt or (D)ecrypt? ").strip().upper()
        message = input("Enter your message: ")

        while True:
            try:
                shift = int(input("Enter shift value: "))
                break
            except ValueError:
                print("Invalid input. Please enter an integer for the shift value.")

        if mode == 'E':
            encrypted_message = encrypt(message, shift)
            print(f"Encrypted message: {encrypted_message}")
            
            # Ask if the user wants to decrypt the same message
            decrypt_choice = input("Would you like to decrypt this message? (Y/N): ").strip().upper()
            if decrypt_choice == 'Y':
                decrypted_message = decrypt(encrypted_message, shift)
                print(f"Decrypted message: {decrypted_message}")

        elif mode == 'D':
            decrypted_message = decrypt(message, shift)
            print(f"Decrypted message: {decrypted_message}")

        else:
            print("Invalid mode selected.")

        # Ask if the user wants to run the program again
        another_choice = input("Would you like to run another encryption/decryption session? (Y/N): ").strip().upper()
        if another_choice != 'Y':
            break

if __name__ == "__main__":
    main()
