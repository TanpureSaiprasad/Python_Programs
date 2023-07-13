#Q.Write a program to accept a number and count number of even, odd, zero digits within that number

n=int(input("Enter Number:"))
ecnt=0
ocnt=0
zcnt=0
while(n>0):
    d=n%10;
    n=n//10;
    if(d==0):
        zcnt=zcnt+1
    elif(d%2==0):
        ecnt=ecnt+1
    else:
        ocnt=ocnt+1
print("Zero Count:",zcnt);
print("Even Count:",ecnt);
print("Odd Count:",ocnt);
