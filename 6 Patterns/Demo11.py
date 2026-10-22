rows = int(input("Enter rows : "));
for i in range(1,rows+1):
    for j in range(1,i+1):
        if j==1 or i==rows or i==j:
            print(j,end="");
        else:
            print(end=" ");
    print();