import random
x = 0
randomno = 0
tails= 0
heads= 0

while x < 50:
    randomno = random.randint(1,2)
    if randomno  == 1:
        print("heads")
        heads = heads + 1
    
    if randomno  == 2:
        print("tails")
        tails = tails + 1
    x = x + 1

print(heads)
print(tails)

  
