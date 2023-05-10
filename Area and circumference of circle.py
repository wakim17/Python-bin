import math
r = float(input("Type a radius for a circle(in cm): "))
circum = 2 * r * math.pi
area = math.pi * r * r
print("The area of your circle is " + str(area) + "cm^2")
print("The circumference of your circle is " + str(circum) + "cm")
