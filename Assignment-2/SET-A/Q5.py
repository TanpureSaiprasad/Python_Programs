'''Q. Write a Python program to get a string from a given string where all occurrences of its first char 
have been changed to '$', except the first char itself. Sample String: 'restart' Expected Result : 'resta$t'.
Ans=>'''

s=input("enter string:")
ch=s[0]
print("Reasult: ",end="")
print(s[0],end="")
for i in range(1,len(s)):
    if ch==s[i]:
        print("$",end="")
    else:
        print(s[i],end="")

