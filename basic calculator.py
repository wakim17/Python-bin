num1=0
num2=0

answer=0
answer2=0
answer3=0
answer4=0


num1= int(input("give me a number "))
num2= int(input("give me another number "))


print ("press 1 to add")

print ("press 2 to substract")

print ("press 3 to divide")

print ("press 4 to multiply")

menu= int(input("which operation should i do "))

if (menu==1):
    answer = num1 + num2
    print(answer)

elif(menu==2):
    answer = num1 - num2
    print(answer)

elif(menu==3):
    answer = num1 / num2
    print(answer)

elif(menu==4):
    answer = num1 * num2
    print(answer)

else:print (error)
    
