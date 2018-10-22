def min(a,b):
    if a<b:
        return a
    else:
        return b

def findmin(st,s,e):
    if s==e:
        return 0
    if s==e-1:
        if st[s] == st[e]:
            return 0
        return 1
    if st[s] == st[e]:
        return findmin(st,s+1,e-1)
    else:
        a = findmin(st,s,e-1)
        b = findmin(st,s+1,e)
        return min(a,b)+1

def main():
    m = int(input())
    st = input()
    print (findmin(st,0,m-1))

main()

