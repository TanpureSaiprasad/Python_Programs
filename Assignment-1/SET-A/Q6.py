#Q.Write a program to calculate sum of first and last digit of a number. 
n=int(input("Enter Number:"))
last=n%10
first=0
while(n>0):
    first=n%10
    n=n//10
    
print("Sum of First & Last digit:",first+last)
