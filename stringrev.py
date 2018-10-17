st = input()
l = []
rev = []
for i in range(0,len(st)):
        l.append(st[i])
i = len(l)-1
while(i >= 0):
    rev.append(l[i])
    i = i - 1
print("".join(rev))
