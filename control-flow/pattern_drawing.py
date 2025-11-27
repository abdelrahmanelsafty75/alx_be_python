num = int(input("Enter the size of the pattern: "))

x = num
while num:
    for i in range(x):
        print("*", end="")
    print()
    num -= 1    