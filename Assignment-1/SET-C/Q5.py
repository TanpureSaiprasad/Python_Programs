#Q.Write python script to accept two numbers as range and display multiplication table of all numbers within that range. 

n=int(input("Enter limit:"))
for i in range(1,n):
    print("Multiplication Table of ",i)
    for j in range(1,11):
        print(i*j)
    
