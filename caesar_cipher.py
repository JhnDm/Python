# caesar_cipher.py

def caesar_cipher_encrypt(message, shift):
    encrypted_message = ""
    for char in message:
        # Encrypt uppercase letters
        if char.isupper():
            encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            encrypted_message += encrypted_char
        # Encrypt lowercase letters
        elif char.islower():
            encrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            encrypted_message += encrypted_char
        else:
            encrypted_message += char  # Keep non-alphabetic characters unchanged
    
    return encrypted_message

def caesar_cipher_decrypt(encrypted_message, shift):
    decrypted_message = ""
    for char in encrypted_message:
        # Decrypt uppercase letters
        if char.isupper():
            decrypted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            decrypted_message += decrypted_char
        # Decrypt lowercase letters
        elif char.islower():
            decrypted_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            decrypted_message += decrypted_char
        else:
            decrypted_message += char  # Keep non-alphabetic characters unchanged
    
    return decrypted_message

# Example usage when running the script directly
if __name__ == "__main__":
    plaintext = "Hello, World!"
    shift_value = 3

    encrypted_text = caesar_cipher_encrypt(plaintext, shift_value)
    print("Encrypted message:", encrypted_text)

    decrypted_text = caesar_cipher_decrypt(encrypted_text, shift_value)
    print("Decrypted message:", decrypted_text)
