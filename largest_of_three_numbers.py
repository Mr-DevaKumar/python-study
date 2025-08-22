#<----Largest of three Numbers----->

# Using if else statement

def largest_if_else(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# Using temporary variable

def largest_temp(a, b, c):
    temp = a
    if b > temp:
        temp = b
    if c > temp:
        temp = c
    return temp

# Using build-in function

def largest_build_in(a, b, c):
    return max(a, b, c)

# Using Sorting

def largest_sorting(a, b, c):
    numbers = [a, b, c]
    numbers.sort()
    largest = numbers[-1]
    return largest

# Combining all functions

def largestOfThreeNumbers():
    print("Largest of Three Numbers")

    while True:
        try:
            a = float(input("Enter first number:"))
            b = float(input("Enter second number:"))
            c = float(input("Enter third number:"))

            print("\n Numbers:", a, b, c)

            result1 = largest_if_else(a, b, c)
            result2 = largest_temp(a, b, c)
            result3 = largest_build_in(a, b, c)
            result4 = largest_sorting(a, b, c)

            print("If-Else:", result1)
            print("Temp Variable:", result2)
            print("Build-in:", result3)
            print("Sorting:", result4)

        except ValueError:
            print("Error: Please enter valid numbers")

largestOfThreeNumbers()