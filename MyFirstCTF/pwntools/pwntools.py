#! /usr/bin/python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 howpwn <finn79426@gmail.com>
#
# Distributed under terms of the MIT license.

from pwn import *

context.log_level = "debug"
# r = remote("140.110.112.29", 2113)
r = process("./pwntools")

r.recvuntil("Give me the magic :)\n")
r.sendline(p32(0x79487ff))
r.recvuntil("Hacker can complete 1000 math problems in 60s, prove yourself.\n")

for i in range(1,1001):
    s = str(r.recvuntil("?").strip()[:-4])
    print s
    answer = str(eval(s))
    print answer
    r.sendline(answer)


r.recvuntil("Welcome hacker!")
r.interactive()
# r.close()
