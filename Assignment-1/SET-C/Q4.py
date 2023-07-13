#Q.Write a program which accept an integer value ‘n’ and display all prime numbers till ‘n’. 

n=int(input("Enter limit:"))
print("Prime Numbers:")
for i in range(2,n):
    f=0
    for j in range(2,i):
        if(i%j==0):
            f=1
    if(f==0):
        print(i)
    
