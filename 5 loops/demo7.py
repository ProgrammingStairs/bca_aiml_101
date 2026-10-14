# example to reverse a number

num = int(input("Enter digits : "))
rev=0
while num>0:
    rem = num % 10;
    rev = rev  * 10 + rem;
    num = num//10;

print("Reverse Number : ",rev);
