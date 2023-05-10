print("I will be checking if the year you type is a leap year")
year = int(input("Enter a year: "))
leapone = year % 4
leaptwo = year % 100
leapfour = year % 400
if leapone == 0:
    if leaptwo == 0:
        if leapfour ==0:
            print(str(year) + " is a leap year")
        else:
            print(str(year) + " isn't a leap year")
    else:
        print(str(year) + " is a leap year")
else:
    print(str(year) + " isn't leap year")
