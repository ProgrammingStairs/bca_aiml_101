# 1
# 12
# 123
# 1234
# 12345

rows = int(input("Enter number of rows : "));
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(j,end="");
    print();