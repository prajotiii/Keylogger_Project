from cryptography.fernet import Fernet

# Function to load the encryption key
def load_key():
    return open("secret.key", "rb").read()

# Function to decrypt the log file
def decrypt_log():
    key = load_key()
    cipher_suite = Fernet(key)
    with open("encrypted_keylog.txt", "rb") as file:
        encrypted_data = file.read()
        decrypted_data = cipher_suite.decrypt(encrypted_data)
    with open("decrypted_keylog.txt", "wb") as file:
        file.write(decrypted_data)

if __name__ == "__main__":
    decrypt_log()
