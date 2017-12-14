#Problem 3: Calculation for the cost of a call started on a certain day and based on the duration

#inputs and variables
weekDay = input("Please enter the day that the call started: ")
startTime = int(input("Please enter the time the call started (hhmm): "))
durTime = int(input("Please enter the duration of the call (minutes): "))
rate = 0.0

#cost calculator
if(weekDay == "Mon" or weekDay == "Tues" or weekDay == "Wed" or weekDay == "Thr" or weekDay == "Fri"):
    if(startTime < 800 or startTime > 1800):
        rate = .25
    else:
        rate = .40
elif(weekDay == "Sat" or weekDay == "Sun"):
    rate = .15

cost = rate * durTime

#print final
#print(rate,durTime,cost)
print("This call will cost $", cost)
