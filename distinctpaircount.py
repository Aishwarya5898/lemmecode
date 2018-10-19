def checkrep(a,b,dic):
    flag = 0
    for key,vals in dic.items():
        if a != key and b != key:
            flag = 1
        else:
            return 0
    return 1

n = int(input())
l= []
d = {}
dic = {}
count = 0
sum = 47
an = 0
for  i in range(0,n):
    s =int(input())
    l.append(s)
for i in range(0,n):
    for j in range(i+1,n):
        if l[i] + l[j] == sum :
            an = checkrep(l[i],l[j],dic)
            if an == 1:
                d = {l[i]:l[j]}
                dic.update(d)
                count = count + 1
                an = 0
            else:
                continue
print(count)
