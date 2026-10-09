# example showing the concept of nested if else statement

a = int(input("Enter value of a : "))
b = int(input("Enter value of b : "))

if a==b:
    print("Both are equal")
else:
    if a>b:
        print(a," is greater")
    else:
        print(b," is greater")
