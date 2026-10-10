# program to check whether entered number is perfect or not

num = int(input("Enter number : "))
sum = 0
for i  in range(1,num//2+1):
    if num%i==0:
        sum = sum + i;
if sum==num:
    print("Number is perfect");
else:
    print("Number is not perfect");