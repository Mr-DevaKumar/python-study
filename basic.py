# <-----Print Function------>

# Basic Input and Output
name = input("What is your name")
print(f"Hello, {name}! Nice to meet you!")

# Using String Formatting
name = input("What is your name")
greeting = "Welcome, {}! Have a nice day!".format(name)
print(greeting)

#<------Basic Calculator------->

def basic_calculator():
    print("Basic Calculator")
    print("Operations: +, -, *, /")
    print("Enter 'quit' to exit")

    while True:
        try:
            num1 = input("Enter the first number (or 'quit'):")
            if(num1.lower == 'quit'):
                break
            operator = input("Enter operator (+, -, *, /):")
            if(operator.lower() == 'quit'):
                break
            num2 = input("Enter the second number:")
            if(num2.lower() == 'quit'):
                break

            num1 = float(num1)
            num2 = float(num2)

            if operator == '+':
                result = num1+num2
            elif operator == '-':
                result = num1-num2
            elif operator == '*':
                result = num1*num2
            elif operator == '/':
                if num2 == 0:
                    print("Error: Division by zero is not allowed!")
                    continue
                result = num1/num2
            else:
                print("Error: Invalid Operator!")
                continue

            print("Result = ", result)
            print("-" * 30)

        except ValueError:
            print("Error: Please enter valid numbers!")
        except Exception as e:
            print("An error occured:", e)

basic_calculator()

#<-----Area of Circle----->

import math

def circle_area():
    print("Circle Area Calculator")
    print("=" * 25)

    while True:
        try:
            radius = input("Enter the radius of the circle (or 'quit' to exit):")

            if(radius.lower() == 'quit'):
                break

            radius = float(radius)

            if(radius < 0):
                print("Error: Radius cannot be zero")
                continue

            area = math.pi * radius ** 2
            print("The area of the circle with radius", radius, "is", area)
            print("-" * 40)

        except ValueError:
            print("Error: Please enter valid numbers!")
        except Exception as e:
            print("An error occured:", e)

circle_area()

#<----Swapping of two variables----->

def swapping():
    print("Swapping of two variables")
    print("-" * 25)

    try:
        a = float(input("Enter the first number"))
        b = float(input("Enter the second number"))
    
    except ValueError:
        print("Using string values")
        a = input("Enter the first variable")
        b = input("Enter the second variable")
    
    print("Original values a = ", a, "b = ", b)

    # Direct swapping 
    a1 , b1 = a , b
    a1 , b1 = b1 , a1
    print("Swapped Values a = ", a1, " b = ", b1)

    # Arithmetic swapping method
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        # Using Addition and Subtraction
        a1 , b2 = a , b
        a2 = a2 + b2
        b2 = a2 - b2
        a2 = a2 - b2
        print("Swapped value using arithmetic operation: a = ", a2, " b = ", b2)
        
        # Using Multiplication and Division
        a3 , b3 = a , b
        a3 = a3 * b3
        b3 = a3 / b3
        a3 = a3 / b3
        print("Swapped using * and / are a = ", a3, " b = ", b3)

        if isinstance(a, int) and isinstance(b, int):
            a4 , b4 = a , b
            a4 = a4 ^ b4
            b4 = a4 ^ b4
            a4 = a4 ^ b4
            print("Swapping using XOR, a = ", a4, " b = ", b4)
swapping()

#<------Temperature Conversion------>

def temperature_converter():
    print("Temperature Converter")
    print("Conversion between:")
    print("1. Celcius to Farenheit")
    print("2. Farenheit to Celcius")
    print("3. Celsius to Kelvin")
    print("4. Farenheit to Kelvin")
    print("5. Kelvin to Celsius")
    print("6. Kelvin to Farenheit")
    print("7. Quit")

    while True:
        try:
            choice = input("Enter your choice")

            if(choice == '7'):
                print("Goodbye")
                break

            if choice not in ['1', '2', '3', '4', '5', '6']:
                print("Please enter a number between 1-7!")
                continue
            temperature = float(input("Enter temperature:"))

            if choice == '1':
                result = (temperature * 9/5) + 32
                print(temperature, "°C = ", result, "°F")

            elif choice == '2':
                result = (temperature - 32) * 5/9
                print(temperature,"°F = ",result, "°C")

            elif choice == '3':
                result = temperature + 273.15
                print(temperature,"°C = ",result, "K")

            elif choice == '4':
                result = (temperature - 32) * 5/9
                print(temperature,"°F = ",result, "K")

            elif choice == '5':
                result = temperature - 273.15
                print(temperature,"K = ",result, "°C")

            elif choice == '6':
                celsius = temperature - 273.15
                result = (celsius * 9/5) + 32
                print(temperature,"K = ",result, "°C")

        except ValueError:
            print("Please enter a valid number")

temperature_converter()

#<-----Odd or Even------>

# Basic Odd or Even

def odd_even():
    print("Even/Odd Number Checker")

    while True:
        try:
            number = input("Enter a number (or 'quit' to exit):")
            if number.lower() == 'quit':
                print("Thank You")
                break
            number = int(number)

            if number % 2 == 0:
                print(number, " is a EVEN number")
            else:
                print(number, " is a ODD number")

        except ValueError:
            print("Error: enter a valid integer")
        except Exception as e:
            print("An error occured", e)

odd_even()

# Using Bitwise Operator

def odd_even_bitwise():
    print("Even/Odd Checker (Using Bitwise Operator)")

    while True:
        try:
            number = input("Enter a number:")

            if number.lower() in ['quit', 'exit', 'q']:
                break
            number = int(number)

            if number & 1:
                print(number, "is ODD number")
            else:
                print(number, " is EVEN number")
        except ValueError:
            print("Please enter a valid integer!")

odd_even_bitwise()


#<----Sum of Digits---->

# Basic Method

def sumOfDigits(n):
    sum = 0
    while n != 0:
        last = n % 10
        sum += last
        n //= 10
    return sum
if __name__ == "__main__":
    n = int(input("Enter a number"))
    print(sumOfDigits(n))

# Using Recursion Function

def sumOfDigits(n):
    if n == 0:
        return 0
    
    return n % 10 + sumOfDigits(n // 10)
if __name__ == "__main__":
    n = int(input("Enter the nume"))
    print(sumOfDigits(n))

# Using String Conversion

def sumOfDigits(n):
    s = str(n)
    sum = 0
    for ch in s:
        sum += int(ch)
    return sum

n = int(input("Enter a number"))
print(sumOfDigits(n))


#<------Remainder without using % operator------>

# Integer Division

def remainder_division(a, b):
    quotient = a // b
    return a - (quotient * b)

a = int(input("Enter first number"))
b = int(input("Enter second number"))
print(remainder_division(a, b))

# Using Repeated Subtraction

def remainder_subtraction(a, b):
    abs_a = abs(a)
    abs_b = abs(b)
    remainder = abs_a
    while remainder >= abs_b:
        remainder -= abs_b
    return -remainder if a < 0 else remainder

a = int(input("Enter first number"))
b = int(input("Enter second number"))
print(remainder_subtraction(a, b))

# Using Bitwise Operator
   # Only can be used when the remainder is the power of 2

def remainder_bitwise(a, b):
    return a & (b - 1)

a = int(input("Enter first number"))
b = int(input("Enter second number"))
print(remainder_bitwise(a, b))