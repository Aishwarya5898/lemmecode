num = int(input())
if num >= 0:
    temp = num
    rev = 0
    while temp != 0:
        rev = rev * 10
        rev = rev + (temp % 10 )
        temp = temp // 10
    print(rev)
else:
    print("Invalid input")
