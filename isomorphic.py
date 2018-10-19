def checklen(a,s1):
    if a == len(s1) - 1:
        print("True")
        exit(1)

def checkdic(d):
    temp = []
    for keys,val in d.items():
        if val not in temp[:]:
            temp.append(val)
        else:
            print("False")
            exit(1)

s = input()
s1 = []
s2 = []
for i in range(0,len(s)):
    if s[i] == ' ':
        continue
    else:
        if ' ' in s[:i]:
            s2.append(s[i])
        else:
            s1.append(s[i])
coun = []
for i in range(len(s1)):
    coun.append(1)
i = len(s1) - 1
while i >= 0:
    if s1[i] in s1[:i]:
        coun[i] = s1.count(s1[i])
    i = i - 1
d = {}
for i in range(0,len(s1)):
    if coun[i] == 1:
        dic = {s1[i]:s2[i]}
        d.update(dic)
checkdic(d)
for i in range(0,len(s1)):
    if len(s1) == len(s2):
        if coun[i] >= 1:
            if d[s1[i]] == s2[i]:
                checklen(i,s1)
            else:
                print("False")
                exit(1)
        else:
            checklen(i,s1)
    else:
        print("False")
        break


