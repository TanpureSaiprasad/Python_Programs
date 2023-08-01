'''Q. Write a python program to count vowels and consonants in a string. 
Ans=>'''

s=input("Enter String:")
vcnt=0
ccnt=0
a1=['a','e','i','o','u','A','E','I','O','U',]
for ch in s:
    if ch in a1:
        vcnt=vcnt+1
    else:
        ccnt=ccnt+1
print("Even Count:",vcnt)
print("Odd Count:",ccnt)
