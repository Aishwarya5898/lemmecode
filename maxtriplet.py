n = int(input())
a  = []
tri = []
for i in range(0,n):
    s = int(input())
    a.append(s)
max = 0
for i in range(0,n):
    for j in range(i+1,n):
        if a[i] != a[j]:
            if a[i]* a[j] > max :
                max = a[i]*a[j]
                c = a[i]
                d = a[j]
tri.append(c)
tri.append(d)
pro = max
for i in range(0,n):
    if a[i] != c and a[i] != d:
        if pro * a[i] > max:
            max = pro * a[i]
            e  = a[i]
tri.append(e)
print(max,"Product is ",tri)
