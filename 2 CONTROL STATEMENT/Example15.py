# How to achieve functionality of switch control statement in python
# 1. if elif
# 2. match
# 3. dictionary

a = int(input("Enter value of a : "))
b = int(input("Enter value of b : "))

print("Select any one option : ");
print("1 for addition");
print("2 for subtraction");
print("3 for multiplication");
print("4 for division");
print("5 for modulus");

choice = int(input("Enter option : "))

if choice==1:
    print("Addition : ",a+b);
elif choice==2:
    print("Subtraction : ",a-b);
elif choice==3:
    print("Multipication : ",a*b);
elif choice==4:
    print("Division : ",a/b);
elif choice==5:
    print("Modulus : ",a%b);
else:
    print("Invalid selection");
        
        