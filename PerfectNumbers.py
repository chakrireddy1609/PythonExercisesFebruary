
sum = 0
for i in range(100,10000):
    for num in range(1,i):
        if (num%i) == 0:
            sum = sum + i
        else:
            continue
if sum == num:
    print("Number is perfect number")
else:
    print("Not a perfect number")