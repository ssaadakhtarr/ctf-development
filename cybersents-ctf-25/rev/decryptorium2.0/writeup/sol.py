enc = bytearray([
    0x74,0x5b,0x5e,0x45,0x08,0x2b,0x05,0x0d,0x5c,0xb7,0x46,0x5d,0x2c,0x07,0x11,0x0d,0x13,0x58,0xae,0x69,0x0b,0x53,0x32,0xa9,0x10,0x1c,0xa6,0x11,0x13,0x13,0x06,0x15,0x70,0x68,0x16,0x2e
])

def reverse_level_three(data):
    for i in range(0, len(data), 2):
        if i + 1 < len(data):
            data[i], data[i+1] = data[i+1], data[i]
    return data

def reverse_level_two(data):
    for i in range(len(data)):
        b = data[i]
        b = (~(b - 1) + 0x100) & 0xFF  # reverse two's complement
        data[i] = b ^ i
    return data

def reverse_level_one(data):
    for i in range(len(data)):
        b = data[i] ^ 0x3C
        data[i] = ((b >> 2) | (b << 6)) & 0xFF
    return data

enc = reverse_level_three(enc)
enc = reverse_level_two(enc)
enc = reverse_level_one(enc)

print(enc.decode())
