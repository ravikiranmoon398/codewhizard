#Wap to convert height from feets in tinches and centimeter

height =float(input("Enter th height-> "))

inch = height * 12
cm = round(inch * 2.54, 1)


print("Height in inch :-",inch)
print("Your height is : %d cm." % cm)
