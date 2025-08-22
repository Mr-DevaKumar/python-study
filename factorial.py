#<----Factorial----->

# Simple Operation
def factorial():
    while(True):
        n = int(input("Enter a number:"))
        fact = 1
        if(n>=1):
            for i in range(1, n+1):
                fact *= i
            print(fact)
        elif(n==0):
            print(1)
        else:
            print("Invalid Input")

factorial()

# Using Recursion

def fact(n):
    return 1 if (n == 1 or n == 0) else n * fact(n-1)

n = int(input("Enter a number:"))
print(fact(n))

# Using Build-in Function

import math 

def factorial(n):
    return math.factorial(n)

n = int(input("Enter a number:"))
print(factorial(n))

# Using numpy function

import numpy

def fact(n):
    return numpy.prod([i for i in range(1, n+1)])

n = int(input("Enter a number:"))
print(fact(n))