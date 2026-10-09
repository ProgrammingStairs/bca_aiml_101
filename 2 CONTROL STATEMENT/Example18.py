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

match choice:
    case 1 : print("Addition : ",a+b);
    case 2 : print("Subtraction : ",a-b);
    case 3 : print("Multipication : ",a*b);
    case 4 : print("Division : ",a/b);
    case 5 : print("Modulus : ",a%b);
    case _ : print("Invalid selection");
        
        