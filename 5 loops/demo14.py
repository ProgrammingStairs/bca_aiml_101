# example to print factorial of all numbers between two numbers

n = int(input("Enter initial number : "))
m = int(input("Enter final number : "))

for i in range(n,m+1):
    fact = 1;
    for j in range(1,i+1):
        fact = fact * j;
    print("Factorial of  ",i," is : ",fact);
    print();    