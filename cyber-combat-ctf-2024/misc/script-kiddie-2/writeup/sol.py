import random
import string
import hashlib

f = open("../chall/chall.txt").read().split("\n")

key_found = False

for i in range(1000):
    if (not key_found):
        key = []
        random.seed(i)
        for i in range(10):
            key.append(random.choice(string.printable))

        for j in string.printable:
            a = hashlib.md5((j + ''.join(key)).encode()).digest().hex()
            if (a == f[0]):
                print(f"[+] Key found: {key}")
                key_found = True
                break
    else:
        break

print(f"[+] Extracting the original file\n\n")

for i in f:
    for j in string.printable:
        check = hashlib.md5((j + ''.join(key)).encode()).digest().hex()
        if check == i:
            print(j, end="")