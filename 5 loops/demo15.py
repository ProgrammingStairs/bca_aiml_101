# example to print factors of all numbers between two numbers

n = int(input("Enter initial number : "))
m = int(input("Enter final number : "))

for i in range(n,m+1):
    print("Factors of ",i)
    for j in range(1,i+1):
        if  i%j==0:
            print(j,end="\t");
    print("\n");    

# Hw
# 1    2    4    7    11......
# 1 + 2 + 3 + 4 + 5 + ........
# 1/1   1/2   1/3   1/4   1/5   1/6 ....
# 0  4  16  36 .....
# 1  9  25  49 .......
  