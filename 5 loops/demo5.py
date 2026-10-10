# program to print fibonacci series

term = int(input("Enter number : "))
a = -1
b = 1
for i  in range(1,term+1):
    c = a + b;
    print(c,end="\t");
    a = b;
    b = c;