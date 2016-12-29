#!/bin/python

import sys

count = 0
n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
a = map(int,raw_input().strip().split(' '))
for i in range(n):
    for j in range(n):
        if(i == j):
            break
        else:
            if (a[i] + a[j])%k == 0:
                count += 1
print count
