import hashlib
from string import printable

inp = open('../chall/chall.txt').read().split('\n')

chars = printable

for i in inp:
    for j in chars:
        check = hashlib.md5(j.encode()).digest().hex()
        if (i == check):
            print(j, end="")