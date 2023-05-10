n = int(input("Enter nth term: "))
summ =0
ts = 0
t=0

while  n >= 1:
    t = n*n
    ts = ts + t
    n = n-1
    summ = ts + n
print(summ)


