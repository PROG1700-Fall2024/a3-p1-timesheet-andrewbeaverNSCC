#Program 1 – Timesheet
#Description:   Design and write a program that accepts the number of hours worked on 
#               each of five work days from the user, then displays different 
#               information calculated about those entries as output. 

#Student #:     W0402993
#Student Name:  Andrew Beaver

def openeningMessage():
    print("Time Sheet Program\n")

def getHoursWorked(working):
    hoursWorked = []
    dayWorked = []
    #establish loop to get inputs of hours worked
    for i in range (working):
        currentDay = float(input("Enter hours on Day #{0}: ".format(i + 1)))
        if currentDay < 0:
            print("WARNING. You cannot work negative hours.")
        hoursWorked.append(currentDay)
        dayWorked.append(i + 1)
    return hoursWorked, dayWorked

def main():
    
    #Establish variables
    slackHours = 7
    numberOfDaysWorked = 5

    openeningMessage()    

    hoursWorked, dayWorked = getHoursWorked(numberOfDaysWorked)

    #Get the max hours and longest day
    mostHours = max(hoursWorked)

    #Print the longest day with most hours to user
    print("\nThe most hours worked was on:")
    for i in range (len(hoursWorked)):
        if hoursWorked[i] == mostHours:
            print("Day #{1} when you worked {0} hours.".format(mostHours, dayWorked[i]))

    #Calculate the total and average hours worked
    totalHours = sum(hoursWorked)
    averageHours = totalHours / len(dayWorked)

    #Display the sum of all hours worked
    print("\nThe total number of hours worked was: {0}".format(totalHours))

    #Display the average hours worked
    print("The average number of hours worked each day was: {0}".format(averageHours))

    #Days less than 7 hours
    print("\nDays you slacked off (i.e. worked less than 7 hours):")
    for i in range (len(hoursWorked)):
        if hoursWorked[i] < slackHours:
            #Specify plurality difference between using hour or hours
            if hoursWorked[i] != 1:
                print("Day #{0}: {1} hours".format(dayWorked[i], hoursWorked[i]))
            else:
                print("Day #{0}: {1} hour".format(dayWorked[i], hoursWorked[i]))

main()