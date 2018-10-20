def created(d,l):
    co = []
    for i in range(0,len(l)):
        co.append(1)
    i = 0
    while i < len(l):
        if l[i] in l[:i]:
            co[i] = l.count(l[i])
        i = i + 1
    for i in range(0,len(l)):
        d[i] = co[i]
    return (d)

def rec(d1,l):
    d1 = created(d1,l)
    flag = 1
    for key, val in d1.items():
        if val != 1:
            l[key] = l[key] + 1
            flag = 0
    if flag == 0:
        d1 = rec(d1, l)
    else:
        return

n = int(input())
l = []
d = {}
for i in range(0,n):
    s = int(input())
    l.append(s)
rec(d,l)
sum = 0
for i in range(0,len(l)):
    sum = sum + l[i]
print(sum)
