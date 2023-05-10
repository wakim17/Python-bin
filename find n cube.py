x = int(input("Input a number of terms: "))
f = 0
while x > 0:
    f = x ** 3
    print("Number is: " + str(x) + " and the cube is " + str(f))
    x = x -1
