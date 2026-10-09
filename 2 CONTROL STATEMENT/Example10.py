# example

chr = ord(input("Enter character : "));

if chr>=65 and chr<=90:
    print("character is in uppercase");
else:
    if chr>=97 and chr<=122:
        print("character is in lowercase");
    else:
        if chr>=48 and chr<=57:
            print("character is a digit");
        else:
            print("invalid character");