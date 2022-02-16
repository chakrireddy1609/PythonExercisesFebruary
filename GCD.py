num1 = 1008
num2 = 909
list = []

if num1 > num2 :
    smallest = num2
else:
    smallest = num1

for i in range(1,smallest+1):
    if num1%i == 0 and num2%i == 0:
        list.append(i)

print(list[-1])
