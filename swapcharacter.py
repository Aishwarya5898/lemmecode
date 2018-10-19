s = input()
l = []
if len(s) % 2 == 0:
    for i in range(len(s)):
        if i % 2 == 0 :
            l.append(s[i+1])
        else:
            l.append(s[i-1])
    print("".join(l))
else:
    print("Invalid")
