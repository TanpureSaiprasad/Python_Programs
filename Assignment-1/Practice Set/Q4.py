#Q.Write a python script to accept the cost price and selling price from the keyboard. Find out if the 
#  seller has made a profit or loss and display how much profit or loss has been made.

cp=int(input("Enter Cost Price:"))
sp=int(input("Enter Selling Price:"))
if(cp==sp):
    print("NO Profit.... NO loss....")
elif(cp<sp):
    print("seller has made a Profit of Rs.",sp-cp)
else:
    print("seller has made a Loss of Rs.",cp-sp)
    
