n = int(input("Enter number for which factorial is needed : "))
factorial = 1
if n == 0:
    print("Factorial is 1")
elif n > 0:
    for i in range(1,n+1):
        factorial = factorial * i
    print(factorial)
else:
    print("Invalid input")

