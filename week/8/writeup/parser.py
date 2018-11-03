#!/usr/bin/env python2

import sys
import struct


# You can use this method to exit on failure conditions.
def bork(msg):
    sys.exit(msg)


# Some constants. You shouldn't need to change these.
MAGIC = 0xdeadbeef
VERSION = 1

if len(sys.argv) < 2:
    sys.exit("Usage: python3 stub.py input_file.fpff")

# Normally we'd parse a stream to save memory, but the FPFF files in this
# assignment are relatively small.
with open(sys.argv[1], 'rb') as fpff:
    data = fpff.read()

# Hint: struct.unpack will be VERY useful.
# Hint: you might find it easier to use an index/offset variable than
# hardcoding ranges like 0:8
magic, version = struct.unpack("<LL", data[0:8])
index = 8
if magic != MAGIC:
    bork("Bad magic! Got %s, expected %s" % (hex(magic), hex(MAGIC)))

if version != VERSION:
    bork("Bad version! Got %d, expected %d" % (int(version), int(VERSION)))

timestamp = struct.unpack("<L",data[index:index+4])[0]
index = index + 4
if not isinstance(timestamp,int):
    bork("YOOOO What you doing this timestamp ain't a valid UNIX timestamp.")

author = struct.unpack("<8s",data[index:index+8])[0]
index = index + 8
try:
    author = author.decode('utf-8')
except Exception:
    bork("YOOOOOOOO This isn't a string.")

section_count = struct.unpack("<L",data[index:index+4])[0]
index = index + 4
if not isinstance(section_count,int):
    bork("YOOOOO THIS ISN'T AN INTEGER STOP THIS MADNESS")
section_count = int(section_count)
if(section_count < 1):
    bork("YOOOO You're section number is less than 1. ")

print("------- HEADER -------")
print("MAGIC: %s" % hex(magic))
print("VERSION: %d" % int(version))
print("TIMESTAMP: %d" % int(timestamp))
print("AUTHOR: %s" % author)
print("SECTION COUNT: %d" % section_count)

# We've parsed the magic and version out for you, but you're responsible for
# the rest of the header and the actual FPFF body. Good luck!

print("-------  BODY  -------")
section_num = 1
while index < len(data):
    stype,slen = struct.unpack("<LL",data[index:index+8])
    if not(isinstance(stype,int)) and not isinstance(slen,int):
        bork("YO you fucked up")
    stype = hex(stype)
    slen = int(slen)
    index = index+8
    if stype == '0x9':
        sdata = struct.unpack((str(slen) + "s"), data[index:index+slen])[0]
        try:
            sdata = sdata.decode('ascii')
        except Exception:
            bork("Incorrect type encoded")
        print("SECTION %d: %s, SECTION TYPE: SECTION_ASCII" %(section_num,sdata))
    elif stype == '0x5':
        i = int(slen/4)
        sdata = struct.unpack((str(i)+"I"),data[index:index+slen])
        sdata = list(sdata)
        sdata = [str(i) for i in sdata]
        print("SECTION %d: %s, SECTION TYPE: SECTION_WORDS" %(section_num,sdata))
    elif stype == '0x3':
        sdata = struct.unpack((str(slen) + "s"), data[index:index+slen])[0]
        try:
            sdata = sdata.decode('utf-8')
        except Exception:
            bork("Incorrect type encoded")
        print("SECTION %d: %s SECTION TYPE: SECTION_UTF8" %(section_num,sdata))
    elif stype == "0x6":
        if slen != 16:
            bork("Incorrect number of bytes.")
        try:
            latitude,longitude = struct.unpack("dd",data[index:index+slen])
        except Exception:
            bork("BAD!")
        print("SECTION %d: (%f,%f), SECTION TYPE: SECTION_COORD" %(section_num,latitude,longitude))
    elif stype == "0x7":
        if slen !=4:
            bork("The reference section must contain only one work!")
        try:
            sdata = struct.unpack("I",data[index:index+4])[0]
        except Exception:
            bork("YOLO")
        sdata = int(sdata)
        if sdata < 0 or sdata > section_count:
            bork("This is not a valid reference")
        print("SECTION %d: This is a pointer pointing to block %d, SECTION TYPE: SECTION_REFERENCE" %(section_num,sdata))
    elif stype == "0x1":
        try:
            sdata = struct.unpack(str(slen) +"s",data[index:index+slen])[0]
        except Exception:
            bork("Bad")
        png = bytes([0x89,0x50,0x4e,0x47,0x0d,0x0a,0x1a,0x0a])
        png += sdata
        png = bytes(png)
        name = "output" + str(section_num) + ".png"
        new_file = open(name,"wb")
        new_file.write(png)
        new_file.close()
        print("SECTION %d: PNG saved to output%d.png, SECTION TYPE: SECTION_PNG" %(section_num,section_num))
    elif stype == "0x2":
        i = int(slen/8)
        sdata = struct.unpack((str(i)+"Q"),data[index:index+slen])
        sdata = list(sdata)
        sdata = [str(i) for i in sdata]
        print("SECTION %d: %s, SECTION TYPE: SECTION_DWORDS" %(section_num,sdata))
    elif stype == "0x4":
        i = int(slen/8)
        sdata = struct.unpack((str(i)+"d"),data[index:index+slen])
        sdata = list(sdata)
        sdata = [str(i) for i in sdata]
        print("SECTION %d: %s, SECTION TYPE: SECTION_DOUBLES" %(section_num,sdata))
    else:
        bork("Unsupported type!")

    print()
    section_num+=1
    index = index + slen
