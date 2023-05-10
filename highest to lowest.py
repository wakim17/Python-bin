numbone = int(input("Enter a number: "))
numbtwo = int(input("Enter another number: "))
numbthree = int(input("Enter one more number: "))
if numbone > numbtwo:
    if numbone > numbthree:
        if numbtwo > numbthree:
            print("The order is " + str(numbone) + "," + str(numbtwo) + "," + str(numbthree))
elif numbtwo > numbthree:
    if numbtwo > numbone:
        if numbone > numbthree:
            print("The order is " + str(numbtwo) + "," +  str(numbone) + "," + str(numbthree))
elif numbthree > numbtwo:
    if numbthree > numbone:
        if numbtwo > numbone:
            print("The order is " + str(numbthree) + "," + str(numbtwo) + "," + str(numbone))