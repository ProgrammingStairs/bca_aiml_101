# example showing the concept of while True + break

while True:
    password = input("Enter password : ");
    if len(password)>6:
        print("invalid");
    else:
        print("valid");
        break;



