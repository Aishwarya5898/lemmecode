n = int(input())
l = []
for i in range(0,n):
    s = int(input())
    l.append(s)
l.sort()
sum = 0
j  = len(l)-1
while j >= 0 :
    sum = sum + (l[j] * 10**(j))
    j = j - 1
print(sum)
