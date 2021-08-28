#WAP to calculate gross salary 

sal = int(input("Enter the salary->"))

HRA =0.3 *sal
TA =0.4*sal 
DA =0.2*sal 

gross = (sal+HRA+TA+DA)
print("Gross Salary is ->",gross)