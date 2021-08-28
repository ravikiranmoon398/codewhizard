#WAP for swapping without using third variable
x = int(input("Enter the value of x ->"))
y = int(input("Enter the value of y ->"))

print("Before Swapping x={} & y={}".format(x,y))

#temp is the third variable

temp = x
x=y
y= temp

print("After Swapping x={} & y={}".format(x,y))