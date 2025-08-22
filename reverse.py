n = int(input("Enter a number to be reversed"))
if(n>=10):
    reverse = str(n)
    print(reverse[::-1])
else:
    print("Enter valid input")