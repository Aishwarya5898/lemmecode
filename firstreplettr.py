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
    if co[i] > 1:
        print(l[i])
        exit(1)
print("Unique")
