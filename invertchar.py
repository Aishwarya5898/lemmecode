l = input()
s = []
for i in range(0,len(l)):
    if l[i] >= '0' and l[i] <= '9':
        print("Invalid")
        exit(1)
    else:
        s.append(l[i])
for i in range(0,len(s)):
    if s[i] == ' ':
        continue
    if ord(s[i]) >= 97 and ord(s[i])<= 112:
       if i == 0 or s[i-1] == ' ':
           s[i] = chr(ord(s[i]) - 32)
print("".join(s))
