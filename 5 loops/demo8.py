# example to check whether entered number is palindrome or not

num = int(input("Enter digits : "))
rev=0
temp = num;
while num>0:
    rem = num % 10;
    rev = rev  * 10 + rem;
    num = num//10;

print("Reverse Number : ",rev);
print("Number : ",num);

if rev == temp:
    print("Number is palindrome");
else : 
    print("Number is not palindrome");










