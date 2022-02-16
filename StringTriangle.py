str = input("Enter the string : ")

for row in range(len(str)):
    for col in range(row+1):
        print(str[col],end="")
    print()