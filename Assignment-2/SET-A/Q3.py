'''Q. Write a Python program to remove the characters which have odd index values of a given string.
Ans=>'''

s=input("Enter Srting:")

'''s1=""
for i in range(1,len(s),2):
    s1=s1+s[i]
print("Given String",s)
print("required String",s1)'''

#----------using list--------------

a1=list(s)
l=len(a1)//2
for i in range(0,l):
    del a1[i]
if(l%10!=0):
    del a1[-1]
print("Given String",s)
print("required String in list",a1)
