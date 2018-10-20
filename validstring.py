
import math
import os
import random
import re
import sys

# Complete the isValid function below.
def getkey(dict,value):
    for key , val in dict.items():
        if dict[key] == value:
            return (key)
def isValid(s):
    d = {}
    d2 = {}
    l = []
    v = []
    for i in range(0,len(s)):
        l.append(s[i])
    for i in range(0,len(l)):
        co = l.count(l[i])
        d[l[i]] = co
    co = 0
    for key,val in d.items():
        v.append(val)
    for i in range(0,len(v)):
        co= v.count(v[i])
        d2[v[i]] = co
    co = 0 
    b  = []
    for key,val in d2.items():
        b.append(val)
    a = max(b)
    k = getkey(d2,a)
    for key,val in d.items():
        if val != k :
            co= co + 1
            va = val
    if co > 1:
        return("NO")
    else:
        if co == 0:
            return ("YES")
        else:
            if va-k == 1 or k-va == 1:
                return("YES")
            else:
                return("NO")
  
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
