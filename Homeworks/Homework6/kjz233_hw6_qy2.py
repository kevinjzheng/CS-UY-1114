#Problem 2a

def print_month_calendar(num_of_days, starting_day):
    x = starting_day
    print("Mon","Tue","Wed","Thr","Fri","Sat","Sun", sep = "\t")
    for j in range(starting_day - 1):
        print(" ", end = "\t")

    for i in range(num_of_days):
        if(x != 7):
            print(str(i+1), end = "\t")
        if(x == 7):
            print(str(i+1), end = "\n")
            x = 0
        x += 1
    #print(x-1)
    print('\n')
    finalPosition = x - 1
    return(finalPosition)

print_month_calendar(31,4)
#print_month_calendar(30,2)

#Problem 2b
def leap_year(year):
    if((year % 4 == 0) and (year % 100 != 0) ):
        return True
    elif(year % 400 == 0):
        return True
    else:
        return False

#Problem 2c
month = ""
def print_year_calendar(year,starting_day):
    for i in range(12):
        if (i == 0):
            month = "January"
            days = 31
        elif (i == 1):
            month = "February"
            if leap_year(year) == True:
                days = 29
            else:
                days = 28
        elif (i == 2):
            month = "March"
            days = 31
        elif (i == 3):
            month = "April"
            days = 30
        elif (i == 4):
            month = "May"
            days = 31
        elif (i == 5):
            month = "June"
            days = 30
        elif (i == 6):
            month = "July"
            days = 31
        elif (i == 7):
            month = "August"
            days = 31
        elif (i == 8):
            month = "September"
            days = 30
        elif (i == 9):
            month = "October"
            days = 31
        elif (i == 10):
            month = "November"
            days = 30
        elif (i == 11):
            month = "December"
            days = 31

        print(month,year)
        starting_day = print_month_calendar(days,starting_day) + 1

#print_year_calendar(2016,5)

#Problem 2d
def main():
    year = int(input('Please enter the year: '))
    starting_day = int(input('Please enter the starting day: '))
    print_year_calendar(year,starting_day)


main()