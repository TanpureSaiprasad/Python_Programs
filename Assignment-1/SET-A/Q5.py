#Q.Write a program to check whether a input number is palindrome or not. 
n=int(input("Enter Number:"))
r=0
num=n
while(n>0):
    d=n%10
    r=(r*10)+d
    n=n//10
    
if(num==r):
    print("Number is Palindron")
else:
    print("Number is not Palindrom")    
