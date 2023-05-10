#addition
x=[[1, 7],[3,6]]
y=[[2, 5],[7,3]]
res=1
for i in range(len(x)):
    for j in range(len(x[0])):
        res[i][j] = x[i][j] + y[i][j]
for r in res:
    print(r)