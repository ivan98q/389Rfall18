#!/usr/bin/env python
#-*- coding:utf-8 -*-

import hashlib
import string

wordlist = open("../probable-v2-top1575.txt", 'r')
hashes = open("../hashes", 'r')

salts = string.ascii_lowercase
hashed = []
for password in wordlist.readlines():
    password = password.strip()
    for salt in salts:
        algo = hashlib.sha512()
        algo.update(salt.encode('utf-8'))
        algo.update(password.encode(wordlist.encoding))
        hashed.append((algo.hexdigest(),password,salt))

count = 1
for toCrack in hashes.readlines():
    toCrack = toCrack.strip()
    for possible_hash in hashed:
        if toCrack == possible_hash[0]:
            print("Password %d is %s with salt %s"%(count,possible_hash[1],possible_hash[2]))
            count = count + 1

