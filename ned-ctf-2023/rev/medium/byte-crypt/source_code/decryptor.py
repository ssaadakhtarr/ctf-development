import zlib
import base64
import os

flag_file = "flag.enc"
if not os.path.exists(flag_file):
    raise FileNotFoundError("Encrypted flag file flag.enc not found!")
with open(flag_file, "r") as file:
    encrypted_flag = file.read().strip()


def super_decryption(encrypted_flag):

    # Step 1: Base64 Decoding
    decoded_data = base64.b64decode(encrypted_flag)

    # Step 2: Zlib Decompression
    decompressed_data = zlib.decompress(decoded_data)

    # Step 3: Reversing
    reversed_data = decompressed_data[::-1]

    # Step 4: XOR Decryption
    key = "CUwRn048*r$gUuE"
    decrypted_flag = ""
    for i in range(len(reversed_data)):
        decrypted_flag += chr((reversed_data[i]) ^ ord(key[i % len(key)]))

    return decrypted_flag

# Decrypt the flag
flag = super_decryption(encrypted_flag)
print(flag)
