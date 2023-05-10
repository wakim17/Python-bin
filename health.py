fever = str(input("Do you have a fever? (Yes(y) or No(n) "))
nose = str(input("Do you have a stuffy nose? (Yes(y) or No(n) "))
rash = str(input("Do you have a rash? (Yes(y) or No(n) "))
ear = str(input("Do your ears hurt? (Yes(y) or No(n) "))
if fever == "n":
    if nose == "n":
        if rash == "n":
            if ear == "n":
                print("You have Hypochondriac")
if fever == "n":
    if nose == "y":
        if rash == "n":
            if ear == "n":
                    print("You have a Head cold")
if fever == "y":
    if nose == "n":
        if rash == "n":
            if ear == "y":
                print("You have an Ear infection")
if fever == "y":
    if nose == "n":
        if rash == "n":
            if ear == "n":
                print("You've caught a flu")
if fever == "y":
    if nose == "n":
        if rash == "y":
            if ear == "n":
                print("You have Measles")
