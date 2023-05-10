a=input(" Enter a word. ")
b=input(" Enter another word. ")
A = len(a)
S = False

for i in range (len(b)):
    if a==b[i:A]:
        print("true")
        S= True
    A = A + 1

if S==False:
    print("false")