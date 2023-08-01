'''Q. Write a python program to count repeated characters in a string. 
Sample string: 'thequickbrownfoxjumpsoverthelazydog' 
Expected output: 
o 4 
e 3 
u 2 
h 2 
r 2 
t 2
Ans=>'''

s=input("Enter String:")
d={}
for ch in s:
    if ch in d:
        d[ch]=d[ch]+1
    else:
        d[ch]=1
for key,val in d.items():
    if val>=2:
        print(key,d[key])
    
