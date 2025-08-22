while(True):
    n = int(input("Enter a number:"))
    if(n>0):
        if(n%2==0):
            print(n, "is a even number")
        else:
            print(n, "is a odd number")
    else:
        print("Invalid Input")