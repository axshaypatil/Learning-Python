'''
Question No 3

Python program to find area of triangle whoes sides are given.

'''
import math

def areaoftriangle(a,b,c):
#checking if the sides can form a triangle
    if a + b > c and a + c > b and b + c > a:
        #calculating semi-perimeter
        semiPeri = (a+b+c)/2
        print(f"Semi perimeter is {semiPeri}")
        #calculating area using Heron's formula
        area = math.sqrt(semiPeri *(semiPeri-a)*(semiPeri-b)*(semiPeri-c))
        print("The area of triangle is: ", area)

#taking input from user(sides of triangle)

a = float(input("Enter the first side of triangle: "))
b = float(input("Enter the second side of triangle: "))
c = float(input("Enter the third side of triangle: "))

areaoftriangle(a,b,c)
