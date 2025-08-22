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
    import calender
    return calender.isleap(year)

def leapYear():
    