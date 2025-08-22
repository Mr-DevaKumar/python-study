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