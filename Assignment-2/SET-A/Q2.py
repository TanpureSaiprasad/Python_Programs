'''Q. Write a python script to count the number of characters (character frequency) in a string. Sample 
String : google.com'. Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}
Ans=>'''

s=input("Enter String:")
a1={}
for ch in s:
    if ch in a1:
        a1[ch]=a1[ch]+1
    else:
        a1[ch]=1
print(a1)
