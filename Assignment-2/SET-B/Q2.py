'''Q. Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string. 
Sample String : 'abc', 'xyz' 
Expected Result : 'xycabz'
Ans=>'''

s1=input("Enter 1st String:")
s2=input("Enter 2st String:")
s3=s1+s2
l=len(s1)
print("Result:",s3[l:l+2],end="")
print(s3[2:l],end="")
print(s1[:2],end="")
print(s3[l+2:])

