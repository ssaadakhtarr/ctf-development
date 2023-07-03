import base64
import zlib
import os

flag_file = "flag.txt"
if not os.path.exists(flag_file):
    raise FileNotFoundError("Flag file flag.txt not found!")
with open(flag_file, "r") as file:
    original_flag = file.read().strip()

def xor_apply(data, key):
    decrypted = ""
    for i in range(len(data)):
        decrypted += chr(ord(data[i]) ^ ord(key[i % len(key)]))
    return decrypted

def super_encryption(encrypted_flag):

    # Step 1: XOR Decryption
    key = "CUwRn048*r$gUuE"
    xored_data = xor_apply(encrypted_flag, key)

    # Step 2: Reversing
    reversed_data = xored_data[::-1]

    # Step 3: Zlib Compression
    compressed_data = zlib.compress(bytes(reversed_data, 'utf-8'))

    # Step 4: Base64 Encoding
    encoded_flag = base64.b64encode(compressed_data)

    return encoded_flag

# print(original_flag)

flag = super_encryption(original_flag)

print(f'Encrypted Flag: {flag}')
