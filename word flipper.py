first = input("Enter your first name: ")
last = input("Enter your last name: ")
x = len(first)
back = ''
w = ''
y = x-1
back_two =''
b = len(last)
a = b-1
m =''
while y >=0:
    back = first[y]
    w = str(w + str(back))
    y = y -1


while a >=0:
    back_two = last[a]
    m = str(m + str(back_two))
    a = a-1
print("Your name backwards is " + str(w.lower()) + " " + str(m.lower()))
