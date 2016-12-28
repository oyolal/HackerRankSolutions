#!/bin/python

import sys


a,b,c,d,e = raw_input().strip().split(' ')
a,b,c,d,e = [int(a),int(b),int(c),int(d),int(e)]
list = [int(a),int(b),int(c),int(d),int(e)]
list.sort()
j = 0
k = 0
for i in range(4):
    j += list[i]
for i in range(1,5):
    k += list[i]
print j, k
