#<----Fibonacci Sequence---->

def fib():
    print("Fibonacci Sequence Generator")

    while True:
        try:
            n = input("How many fibonacci number to be generated (or 'quit' to exit):")

            if n.lower() == 'quit':
                print("Thank You, Come Again")
                break

            n = int(n)

            if n <= 0:
                print("Please enter a positive number")
                continue

            fib_sequence = []
            a, b = 0, 1

            for i in range(n):
                fib_sequence.append(a)
                a, b = b, a + b

            print(fib_sequence)
        
        except ValueError:
            print("Error: Please enter the valid input")

        except Exception as e:
            print("An error occured:", e)

fib()