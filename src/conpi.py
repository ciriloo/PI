#!usr/bin/python
import pi
import sys
l=3.1415926535897931159979634685441852
i=0
n=int(sys.argv[1])
print 'i     PI35DT                lista i                 PI35DT - lista i'
veces=int(sys.argv[2])
for i in range(veces):
 s=pi.pi(n)
 print '%i     %f               %f                   %f'   % (i,l,s,s-l)
 n=n+1