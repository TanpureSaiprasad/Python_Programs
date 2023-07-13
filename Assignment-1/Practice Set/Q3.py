#Q.Write python script to accept the x and y coordinate of a point and find the quadrant in which the point lies.

x=int(input("Enter X coordinate:"))
y=int(input("Enter Y coordinate:"))
if(x>0 and y>0):
    print("Point Lies In 1st Quadrant")
elif(x<0 and y>0):
    print("Point Lies In 2nd Quadrant")
elif(x<0 and y<0):
    print("Point Lies In 3rd Quadrant")
elif(x>0 and y<0):
    print("Point Lies In 4th Quadrant")
else:
    print("Point Lies In origin(0,0)")
