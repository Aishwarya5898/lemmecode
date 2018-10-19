dict = { 'I': 1, 'V': 5 , 'X':10}
s = input()
val = 0

for i in range(len(s)):
    if s[i] not in dict:
        print("Invalid")
        exit(1)
i = 0
while(i<len(s)):
    if(i+1 < len(s)):
        if(dict[s[i]]>= dict[s[i+1]]):
            val = val + dict[s[i]]
            i = i + 1
        else:
            val = val + dict[s[i+1]]-dict[s[i]]
            i = i + 2
    else:
        val = val + dict[s[i]]
        i = i + 1
print(val)
