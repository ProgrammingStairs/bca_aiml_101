# *
# ***
# *****
# *******
# *********

#    2     4    6    8    10 ...... 2 x i where i = 1,2,3,4,5,....
#  1    3    5    7    9 ...... 2 x i - 1 where i = 1,2,3,4,5,....

rows = int(input("Enter number of rows : "));
for i in range(1,rows+1):
    for j in range(1,2*i):
        print("*",end="");
    print();

