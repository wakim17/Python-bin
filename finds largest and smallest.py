n = [3,41,26,12,9,74,15]
b = 0
d=0
f= 0
m =99999
for e in n:
    if b < e:
        b = e
    if m > e:
        m = e
  

print("Largest number: " + str(b))
print("Smallest number: " + str(m))
