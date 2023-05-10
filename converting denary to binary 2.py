a = list(input("Input a binary number: "))
num = 0

for i in range(len(a)):
    digit = a.pop()
    if digit == '1':
        num = num + pow(2, i)
print(num)