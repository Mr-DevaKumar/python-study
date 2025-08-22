#<----Leap Year----->

# if else condition

def leap_year_if_else(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return False
    else:
        return False

# Build-in

def leap_year_build_in(year):
    import calender # type: ignore
    return calender.isleap(year)

def leapYear():
    print("Leap Year Calculation")
    while True:
        try:
            year = input("Enter a year (or 'quit' to exit):")

            if year.lower() == 'quit':
                print("Thank You")
                break

            year = int(year)

            print(leap_year_if_else(year))
            print(leap_year_build_in(year))

        except ValueError:
            print("Error: Please enter a valid year")
        except Exception as e:
            print("An error occured ", e)

leapYear()
