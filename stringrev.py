st = input()
l = []
rev = []
for i in range(0,len(st)):
    if((st[i] <= '90' and st[i] >= '65' ) or (st[i] >= '97' and st[i] <= '112')):
        l.append(st[i])
    else:
        print("Invalid input")
        exit(1)
i = len(l)-1
while(i >= 0):
    rev.append(l[i])
    i = i - 1
print("".join(rev))
