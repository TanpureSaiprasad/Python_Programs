'''Q. Write a python script to display alternate characters of string from both the direction.
ans=>'''

s=input("Enter String:")
print("Alernate Character from Left to Right:")
for i in range(0,len(s),2):
    print(" ",s[i],end="")
print("\nAlernate Character from Right to Left:")
for i in range(len(s)-1,0,-2):
    print(" ",s[i],end="")
    
    
