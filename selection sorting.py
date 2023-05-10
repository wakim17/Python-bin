Array=[6,4,23,15,7]
for i in range(len(Array)):
    min_index = i
    for j in range(i, len(Array)):
        if Array[j] < Array[min_index]:
            min_index = j
    Array[i], Array[min_index] = Array[min_index], Array[i]

print (Array)
