#!/usr/bin/env python
import hashlib

file1 = open('/home/yassen/penetrationTesting/Testthings/Any_Thing/password.txt', 'r')
Lines = file1.readlines()
file2 = open('/home/yassen/penetrationTesting/Testthings/Any_Thing/password-hashing2.txt', 'w')

for i in Lines:
    md5hash = hashlib.md5(i.rstrip().encode())
    print(i.rstrip())
    print(md5hash.hexdigest())
    file2.write(i)
    file2.write(md5hash.hexdigest())
    file2.write("\n")
file2.close()