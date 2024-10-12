# PRODIGY_CS_01 - Caesar Cipher Implementation 🔐

This Python project implements a **Caesar Cipher** as a command-line tool for both encrypting and decrypting messages. The user is prompted to choose an operation (encryption or decryption), enter their message, and specify a key to shift characters. The program then outputs the result based on the user's input. 🎉

## ✨ Features

- **Encryption**: Convert a plain text message into a secret code 🔏.
- **Decryption**: Decode an encrypted message back to its original form 📝.
- **Customizable Key**: The key specifies how many positions the characters will shift.

## 🚀 How It Works

The implementation revolves around a loop in the main function, where the user is repeatedly asked to:

1. Choose whether to encrypt or decrypt a message.
2. Input the message to be processed.
3. Provide a key for shifting the characters (i.e., how many positions to shift in the alphabet).

### Caesar Cipher Explanation 🧠

The **Caesar Cipher** is a type of substitution cipher where each letter in the plaintext is shifted by a number of positions down or up the alphabet based on the given key. For example, with a shift of `3`:
- 'A' becomes 'D'
- 'B' becomes 'E'
- and so on...

For decryption, the process is reversed using the same key.


## 🛠️ How to Use

1. Clone the repository:
   ```bash
   https://github.com/Pranav18s/python-project-encryption.git
   
2. Run the script:
   ```bash
    python caesar_cipher.py
