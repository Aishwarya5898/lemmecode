n = int(input())
m = int(input())
l1 = []
l2 = []
flag1 = 1
for i in range(0,n):
    s = int(input())
    l1.append(s)
for i in range(0,m):
    s = int(input())
    l2.append(s)
for j in range(0,m):
    if l2[j] in l1:
        flag = 1
    else:
        flag1 = 0
if flag1 == 0 :
    print("NO")
else:
    print("YES")
