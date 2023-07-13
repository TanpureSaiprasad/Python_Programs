#Q.Write a program to calculate base X to power y.
x=int(input("Enter base X:"))
y=int(input("Enter exponent Y:"))
p=1
for i in range(y):
    p=p*x
print("X rais to the power of Y:",p)

