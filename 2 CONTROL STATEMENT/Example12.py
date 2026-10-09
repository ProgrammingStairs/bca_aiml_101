# example to find out grade
# per>=75 and per<=100 Grade A 
# per>=60 and per<75   Grade B 
# per>=50 and per<60   Grade C 
# per>=33 and per<50   Grade D
# fail

# m1 = int(input("Enter marks of m1 : "));
# m2 = int(input("Enter marks of m2 : "));
# m3 = int(input("Enter marks of m3 : "));
# m4 = int(input("Enter marks of m4 : "));
# m5 = int(input("Enter marks of m5 : "));

m1,m2,m3,m4,m5 = map(int,input("Enter marks : ").split())

total = m1+m2+m3+m4+m5;
print("Total marks : ",total);

per = total/5;
print("Percentage : ",per);

if per>=75 and per<=100:
    print("Grade A");
elif per>=60 and per<75:
    print("Grade B");
elif per>=50 and per<60:
    print("Grade C");
elif per>=33 and per<50:
    print("Grade D");
else:
    print("Fail");