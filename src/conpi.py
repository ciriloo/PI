#!usr/bin/python
import pi
import sys
l=3.1415926535897931159979634685441852
k=[]
i=1
n=int(sys.argv[1])
print 'i     PI35DT                lista i                 PI35DT - lista i'
veces=int(sys.argv[2])
for i in range(1,veces+1):
 s=pi.pi(n*i)
 print '%i     %.10f               %.10f                   %.10f'   % (i,l,s,s-l)
 n=n+1
 k=k+[s]
print ' la lista de las aproximaciones es: '
print k