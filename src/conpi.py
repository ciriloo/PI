#!usr/bin/python
import pi
import sys
l=[]
i=0
n=int(sys.argv[1])
veces=int(sys.argv[2])
for i in range(veces):
 s=pi.pi(n)
 l=l+[s]
 n=n+1
print l