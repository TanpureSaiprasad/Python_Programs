'''1. Write a python script which accepts 5 integer values and prints “DUPLICATES” if any of the 
values entered are duplicates otherwise it prints “ALL UNIQUE”. Example: Let 5 integers are (32, 
45, 90, 45, 6) then output “DUPLICATES” to be printed.
Ans=>'''

n=int(input("Enter Limit:"))
a1=[]
for i in range(0,n):
    num=int(input("Enter Number:"))
    a1.append(num)
a2=set(a1)

if(len(a2)==n):
  print("All Unique")
else:
  print("Duplicate")
   
