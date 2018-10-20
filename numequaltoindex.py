n = int(input())
l = []
for i in range(0,n):
    s = int(input())
    l.append(s)
res = []
for i in range(0,len(l)):
    if i == l[i]:
        res.append(l[i])
if res == []:
    print("-1")
    exit(1)
res.sort()
for i in range(0,len(res)):
    print(res[i],end = " ")
