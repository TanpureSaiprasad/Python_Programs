#A cashier has currency notes of denomination 1, 5 and 10. Write python script to accept the amount to 
#be withdrawn from the user and print the total number of currency notes of each denomination the cashier will have to give.
rs=int(input("Enter Amount:"))
ten=rs//10
rs=rs%10
five=rs//5
rs=rs%5
one=rs//1
print("Ten rupees Notes:",ten)
print("Five rupees Notes:",five)
print("One rupees Notes:",one)
