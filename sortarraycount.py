def getval(dic,val):
    for key,v in dic.items():
        if dic[key] == val:
            del dic[key] #since there are duplicates in values , delete the key and its value
            return key

l = []
so= []
d = {}
dic = {}
val = []
n = int(input()) # 7
for i in range(0,n):
    s = int(input()) #get the input(4 5 5 3 6 4 5 )
    l.append(s)
l.sort() #sort the input (3 4 4 5 5 5 6)
co = []
for i in range(0,len(l)):
    co.append(l.count(l[i])) #get the occurence count of each num 1 2 2 3 3 3 1
for i in range(0,len(l)):
    d = {i:co[i]} """dictionary on index of l list as key(for uniqueness)
    its count as value since the input cant be the key as it has multiple value"""
    dic.update(d)
for a,b in dic.items():
    val.append(b) #reverse the process ie get the key from value , so sort the count array first
val.sort() # 1 1 2 2 3 3 3 count sorted
for v in val:
    print(l[getval(dic,v)]) #call the function to get the key
