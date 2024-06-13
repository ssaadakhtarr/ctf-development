import base64
import hashlib
import os

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

def level1_decrypt(data):
    return level1_encrypt(data)  # XOR with the same key will decrypt

def level2_decrypt(data):
    return level2_encrypt(data)  # XOR with the same key will decrypt

def level3_decrypt(data):
    return level3_encrypt(data)  # XOR with the same key will decrypt


def decrypt(data):
    data = base64.b64decode(data)
    data = level3_decrypt(data)
    data = level2_decrypt(data)
    data = level1_decrypt(data)
    return data.decode()


a = input("Enter text to decrypt: ")
res = decrypt(a)
print(res)