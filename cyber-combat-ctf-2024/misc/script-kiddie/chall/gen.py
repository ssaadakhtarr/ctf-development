import hashlib

desc_with_flag = open('description.txt').read()
out = []
out_file = open('chall.txt', 'w+')

for i in desc_with_flag:
    out.append(hashlib.md5(i.encode()).digest().hex())

for j in out:
    out_file.write(j + '\n')

out_file.close()