"""

Question No 2

write an python program to convert the tempreture in degree centigrade to farenheit

"""

#Taking Input from user

operation = int(input("Enter the operation you want to perform :  1 for Centigrade to Farenheit , 2 for Farenheit to Centigrade : "))

#Choose Operation to perform
if operation == 1:
    centigrade = float(input("Enter the temperature in centigrade: "))
    farenheit = (centigrade * 9/5) + 32
    print(f"{centigrade} centigrade is equal to {farenheit}")

elif operation == 2:
    farenheit = float(input("Enter the temperature in farenheit: "))
    centigrade = (farenheit - 32) * 5/9
    print(f"{farenheit} farenheit is equal to {centigrade}")

else:
    print("Invalid operation")
