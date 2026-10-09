# example to find out greater number among three numbers 

a = int(input("Enter value of a : "))
b = int(input("Enter value of b : "))
c = int(input("Enter value of c : "))

if a>b:
    if a>c: 
        print(a," is greater");
    else:
        print(c," is greater");
else:
    if b>c:
        print(b," is greater");
    else:
        print(c," is greater");