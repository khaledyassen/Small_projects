#!/usr/bin/python3

#Read content form file 
file2 = open('/home/yassen/penetrationTesting/Testthings/Any_Thing/smallTest.txt','r')
print("Content of file will display now ")
print("\n")
for value in file2:
  print(value)
file2.close()

# Hashing 
import hashlib
secret = "THis is secret words hack your family is not good idea"
hash_secret = hashlib.sha256(secret.encode('utf-8')).hexdigest()
print(f"Value of hasing for secret message is {hash_secret}")

