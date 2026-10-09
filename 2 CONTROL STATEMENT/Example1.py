# Example to find out simple interest

p=int(input("Enter p : "))
r=float(input("Enter r : "))
t=int(input("Enter t : "))

si = (p*r*t)/100
print("Simple interest : ",si)

amt = p * pow(1+r/100,t)
ci = amt - p

print("Amount : ",amt)
print("Compound interest : ",ci)