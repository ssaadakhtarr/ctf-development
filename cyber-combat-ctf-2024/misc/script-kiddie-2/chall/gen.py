import random
import string
import hashlib

desc_with_flag = open('description.txt').read()
out = open('chall.txt', 'w+')

for i in range(1000):
    seed = random.randint(0,1000)
    random.seed(seed)

key = []

for i in range(10):
    key.append(random.choice(string.printable))

for i in desc_with_flag:
    a = hashlib.md5((i + ''.join(key)).encode()).digest().hex()
    out.write(a + '\n')

out.close()