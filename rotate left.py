#moves everything in an array to the left side

Array =[2,3,4]
temp = Array[0]

for i in range (len(Array)):
    if i + 1 < len(Array):
         Array[i] = Array[i+1]
Array[len(Array) - 1] = temp
print (Array)