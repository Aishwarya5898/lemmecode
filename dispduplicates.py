n = int(input())
l = []
for i in range(0,n):
    s = int(input())
    l.append(s)
co = []
for i in range(0,len(l)):
    co.append(1)
for i in range(0,len(l)):
    co[i] = l.count(l[i])
d = {}
for i in range(0,len(l)):
    d[l[i]] = co[i]
res = []
for key,val in d.items():
    if val > 1:
        res.append(key)
res.sort()
for i in range(0,len(res)):
    print(res[i],end =" ")
