# program to find out factors of a number

num = int(input("Enter number : "))
for i  in range(1,num+1):
    if num%i==0:
        print(i,end="\t");