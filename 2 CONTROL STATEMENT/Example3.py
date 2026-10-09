# Example to swap two numbers
# without using third variable

a = int(input("Enter a : "))
b = int(input("Enter b : "))

print("Before swapping : ")
print("a : ",a)
print("b : ",b)

# a = a+b 
# b = a-b
# a = a-b

a = a*b 
b = int(a/b)
a = int(a/b)

print("After swapping : ")
print("a : ",a)
print("b : ",b)

