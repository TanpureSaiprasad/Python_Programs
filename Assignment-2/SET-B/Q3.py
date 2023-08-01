'''Q.Write a Python program to count the occurrences of each word in a given sentence.
Ans=>'''

s=input("Enter String:")
a1=s.split( )
a2={}
for i in a1:
    if i in a2:
        a2[i]=a2[i]+1
    else:
        a2[i]=1
print(a2)


