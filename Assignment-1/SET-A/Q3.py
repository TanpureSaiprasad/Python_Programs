#Q.Write python script to check whether a input number is perfect number of not. 
n=int(input("Enter Number:"))
s=0
for i in range(1,n):
    if(n%i==0):
        s=s+i
    
if(n==s):
    print("Parfect Number")
else:
    print("Not pefect Number ")    
