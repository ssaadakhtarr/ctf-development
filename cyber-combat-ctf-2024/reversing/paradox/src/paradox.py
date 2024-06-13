# Use the Docker image to compile the code.
# I compiled the code using `pyinstller --onefile paradox.py`.


import base64
import hashlib
import time

def xor_encrypt(data, key):
    key_length = len(key)
    return bytes(data[i] ^ key[i % key_length] for i in range(len(data)))

def level1_encrypt(data):
    key = hashlib.sha256("theycallmeeasy".encode()).digest()
    return xor_encrypt(data, key)

def level2_encrypt(data):
    key = hashlib.sha256("iamthemiddleone".encode()).digest()
    return xor_encrypt(data, key)

def level3_encrypt(data):
    key = hashlib.sha256("thinkofmeastheboss".encode()).digest()
    return xor_encrypt(data, key)

def encrypt(data):
    data = level1_encrypt(data)
    data = level2_encrypt(data)
    data = level3_encrypt(data)
    return base64.b64encode(data).decode()

def decrypt(data):
    print("[+] Getting the key")
    time.sleep(1)
    print("[+] Trying the key")
    time.sleep(2)
    print("[+] Finalizing the payload")
    time.sleep(1)
    print("[+] Producing output")
    time.sleep(2)
    return "You really thought It'll be this easy?\nDecrypt is broken and you can't do anything about that."

def main():
    while True:
        print("Choose an option:")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            plain_text = input("Enter the text to encrypt: ")
            encrypted_text = encrypt(plain_text.encode())
            print(f"Encrypted text: {encrypted_text}")
        elif choice == '2':
            encrypted_text = input("Enter the text to decrypt: ")
            print("Decrypting...")
            try:
                plain_text = decrypt(encrypted_text)
                print(f"{plain_text}")
            except Exception as e:
                print(f"Error during decryption: {e}")
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
