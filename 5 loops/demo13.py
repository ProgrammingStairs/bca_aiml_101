# example to print table of all numbers between two numbers

n = int(input("Enter initial number : "))
m = int(input("Enter final number : "))

for i in range(n,m+1):
    print("Table of : ",i);
    for j in range(1,11):
        print(i," x ",j," = ",i*j);
    print();    