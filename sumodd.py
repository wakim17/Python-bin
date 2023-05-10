n= int(input("input a number: "))
Sum = 0

if n <= 0:
    Sum = -1
else:
    for x in range (1 , n + 1):
        Sum = Sum + 2 * x - 1
print (Sum)
