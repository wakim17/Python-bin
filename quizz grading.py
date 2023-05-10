score = int(input("Enter the amount of points you got for your quiz\n(Out of 5): "))
if score == 5:
    print("You get an A!")
elif score == 4:
    print("You got a B")
elif score == 3:
    print("You got a C")
elif score == 2:
    print("You got a D")
elif score <= 1:
    print("You got a F, YOU IS DUMB!")
