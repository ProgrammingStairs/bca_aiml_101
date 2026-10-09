# example

chr = input("Enter character : ");

if chr>="A" and chr<="Z":
    print("character is in uppercase");
else:
    if chr>="a" and chr<="z":
        print("character is in lowercase");
    else:
        if ord(chr)>=48 and ord(chr)<=57:
            print("character is a digit");
        else:
            print("invalid character");