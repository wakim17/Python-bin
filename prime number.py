x= int(input("Enter a number: "))
thing = 2
b =0
while thing <x:
    if (x % thing) ==0:
        print(str(x) + " is not a prime number")
        b =1
    thing = thing +1

if b== 0:
    print(str(x) + " is a prime number")

