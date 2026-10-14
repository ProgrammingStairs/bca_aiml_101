# example showing the concept of nested loop

for i in range(1,4):
    print("i : ",i);
    for j in range(1,4):
        if i==2 and j==2:
            continue;
        print("\tj : ",j);    