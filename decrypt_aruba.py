#!/usr/bin/python
import sys
import pyDes  

hashes = ['0fae97b6252bb98f5806d1242e7083f3']
if (len(sys.argv) > 1):
 hashes = sys.argv
 del hashes[0];
else:
 print "User: admin "
key = (  
 '\x32\x74\x10\x84\x91\x17\x75\x46\x14\x75\x82\x92'  
 '\x43\x49\x04\x59\x18\x69\x15\x94\x27\x84\x30\x03'  
)  
for h in hashes:  
 d = pyDes.triple_des(key, pyDes.CBC, h.decode('hex')[:8], pad='\00')  
 print h, '=>', d.decrypt(h.decode('hex')[8:])  
