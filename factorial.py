num = int(input())
n = num
if(num == 0 or num == 1 ):
    print ("1")
    exit(1)
elif num > 1 :
    while num > 1:
        n = n * (num - 1)
        num = num - 1
    print (n)
else:
    print("Invalid input")
