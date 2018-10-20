n = int(input())
l = []
flag = 0
for i in range(0,n):
    s = int(input())
    l.append(s)
co = []
for i in range(0,len(l)):
    co.append(0)
for i in range(0,len(l)):
    co[i] = l.count(l[i])
for i in range(0,len(l)):
    if co[i] > 2 :
        print("No")
        exit(1)
    if co[i] == 1:
        flag = flag + 1
        a = l[i]
if flag > 1:
    print("No")
