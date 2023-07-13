#Q.Write a python script to accepts annual basic salary of an employee and calculates and displays the Income tax as per the following rules. 
#  Basic: < 2,50,000 Tax = 0
#  Basic: 2,50,000 to 5,00,000 Tax = 10% 
#  Basic: > 5,00,000 Tax = 20%

sal=int(input("Enter Employee Besic Salary:"))
if(sal>=500000):
    print("Basic Salary:",sal)
    print("Income Tax:",sal*20/100)
elif(sal<500000 and sal>=250000):
    print("Basic Salary:",sal)
    print("Income Tax:",sal*10/100)
else:
    print("Basic Salary:",sal)
    print("Income Tax:0")
