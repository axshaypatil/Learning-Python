#Defining Fuction For Simple Interest

def si(p,r,t):
    I = (p*r*t)/100
    return I

#Taking input


p = float(input("Enter the principal amount: "))
r = float(input("Enter the rate of interest: "))
t = float(input("Enter the time period: "))

#Calculating and printing the result
print("Simple Interest is: ",si(p,r,t))