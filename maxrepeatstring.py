string = []
count = 1
l = []
a = input ('hi:')
for i in range(0,len(a)):
    l.append(a[i])
l.append("$")
j = 0
c = 0
maxcount = 0
for i in range(0,len(l)):
    if l[i] == ",":
        count = count + 1
for i in range(0,count):
    string.append([])

for i in range(0,count):
    while (l[j] != "$"):
        string[i].append(l[j])
        if (l[j+1] == ","):
            j = j + 2
            break
        else:
            j = j + 1

for i in range(0,count):
    c =  0
    for j in range(0,count):
        if(set(string[i]) == set(string[j])):
            c =  c + 1
            if c > maxcount :
                maxcount = c
                s = string[i]
print("".join(s))



