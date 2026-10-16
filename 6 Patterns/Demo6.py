# 1
# 23
# 456
# 78910

rows = int(input("Enter number of rows : "));
a = 1
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(a,end=" ");
        a = a + 1;
    print();

#   1   2   3   4   5   6   7   8   9   10 .....
# a=1             a = a+1