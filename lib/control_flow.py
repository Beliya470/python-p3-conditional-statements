#!/usr/bin/env python3

def admin_login():
    username = input ("What's your username?: ")
    password = int(input ("What's your password?: "))
    if (username == "admin" or username =="ADMIN") and password == 12345:
            print ("Access Granted")
    else:
            print ("Access Denied")
            #To test the function
admin_login ()



def hows_the_weather(temperature):
    if temperature < 40:
        print ("It's brisk out there!")
    elif temperature >= 40 and temperature < 60:
        print ("It's a little chilly out there!")
    elif temperature > 85:
        print ("It's too dang hot out there!")
    else:
        print ("It's Perfect out there")
#test the code
temperature = int(input ("What's the temperature?: "))
hows_the_weather(temperature)



def fizzbuzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return number

# Test the function
for i in range(1, 16):  # testing numbers 1 through 15
    print(fizzbuzz(i))


def calculator(operation, num1, num2):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        # To prevent division by zero
        if num2 == 0:
            print("Cannot divide by zero!")
            return None
        return num1 / num2
    else:
        print("Invalid operation!")
        return None

# Examples:
print(calculator("+", 5, 3))  # Output: 8
print(calculator("-", 5, 3))  # Output: 2
print(calculator("*", 5, 3))  # Output: 15
print(calculator("/", 5, 3))
