#!/usr/bin/env python
#-*- coding:utf-8 -*-

# importing useful libraries -- feel free to add any others you find necessary
import socket
import hashlib
import re

host = "142.93.117.193"   # IP address or URL
port = 7331      # port

# use these to connect to the service
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

# receive some data
data = s.recv(1024)
data = data.decode('utf-8')
while("CMSC389R" not in data):
    regex = 'Find me the (\w+) hash of (\w+)'
    matches = re.finditer(regex,data, re.MULTILINE)
    hash_type = None
    to_hash = None
    for matchnum, match in enumerate(matches):
        hash_type = match.group(1)
        to_hash = match.group(2)
        print(data)
        print("Hash Type: " + hash_type)
        print("To Hash: " + to_hash)
    if hash_type == None or to_hash == None:
        print("FAILED TO FIND MATCH")
    else:
        algo = hashlib.new(hash_type)
        algo.update(to_hash.encode('utf-8'))
        hashed = algo.hexdigest() + "\n"
        print(hashed)
        s.send(hashed.encode('utf-8'))
    data = s.recv(1024)
    data = data.decode('utf-8')
print(data)
# close the connection
s.close()
