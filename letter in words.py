l = ['alpha', 'beta', 'gamma', 'epsilon']
x = input("Enter a letter to check: ")
print("The words that contain the letter are: ")
for e in l:
    if str(x) in e:
        print(e)
