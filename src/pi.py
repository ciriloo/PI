#!usr/bin/python
def pi(n):
 PI=0
 while n<=0:
   n=int(raw_input('Valor de n (debe ser mayor que 0):'))
  # print 'n debe ser mayor que 0'
 for i in range(1,n+1):
   x=(i-.5)/float(n)
 #print x
   fx=4/(1+(x*x))
 # print fx
   PI=PI+(fx)/n 
  # print 'subintervalo: [%3.2f,%3.2f] x: %f fx: %6.5f '    %  ((i-1)/float(n), i/float(n), x, fx)
 return PI
 #print 'El valor de PI con 35 decimales :  3.1415926535897931159979634685441852'