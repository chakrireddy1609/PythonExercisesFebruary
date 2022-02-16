
for i in range(0, 1001):
    num = i
    result = 0
    n = len(str(i))
    while(i!=0):
        last_digit = i%10
        result = result + (last_digit ** n)
        i = i//10
    if num == result:
        print(num)