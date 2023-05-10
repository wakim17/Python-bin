quizone = int(input("What result did you get on your first quiz(as a percentage) "))
quiztwo = int(input("What result did you get on your second quiz(as a percentage) "))
quizthree = int(input("What result did you get on your three quiz(as a percentage) "))
quizfour = int(input("What result did you get on your four quiz(as a percentage) "))
avgsum = quizone + quiztwo + quizthree + quizfour
avg = avgsum / 4
if avg >70:
    print ("Your average score for the four exams is " + str(avg) + ". That's higher average!")
elif avg > 50:
    print ("Your average score for the four exams is " + str(avg) + ". That's a pass!")
else:
    print("Your average score for the four exams is " + str(avg) + ". Fuckin Dumbass!")
