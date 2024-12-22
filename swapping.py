'''
Question no 4

Using input function take two numbers and then swap the numbers

'''

#Taking input from user 

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

print(f"first number is {number1} and second number is {number2} before swapping")

#Swapping the numbers using temporary variable

tempVar = number1
number1 = number2
number2 = tempVar

#Printing Results

print(f"first number is {number1} and second number is {number2} after swapping")