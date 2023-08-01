'''Write a python script to create a list and display the list element in reverse order 

Ans=>'''
#Using 4 way display the list element in reverse order

a=[10,20,30,40,50,60]

#1.using reverse Function
#  a.reverse()
#  print(a)

#2.Using For-loop
#for i in range(len(a),0,-1):
#   print(a[i-1])

#3.using List Reversed Function
#print(list(reversed(a)))

#4.Using Slicing
for i in range(len(a),0,-1):
   print(a[i-1:i])
