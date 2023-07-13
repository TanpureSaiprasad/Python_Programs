#Q.Write python script to check whether a input number is Armstrong number or not.
n=int(input("Enter Number:"))
s=0
num=n
while(n>0):
    d=n%10
    s=s+(d*d*d)
    n=n//10
    
if(num==s):
    print("Number is armstrong")
else:
    print("Number is not armstrong")    
