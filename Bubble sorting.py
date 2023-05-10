
Ans=input("Do you want to sort in ascending(a) or descending(d) order?")

if Ans == "a":
    #descending order
    array = [6,4,2,0,9]
    n = len(array)
    for i in range (n):
      for j in range(n-1):
            if array[j] > array [j+1] :
                array[j], array[j+1] = array[j+1], array[j]
    print (array)

if Ans == "d":
    #ascending order
    array = [6,4,2,0,9]
    n = len(array)
    for i in range (n):
        for j in range(n-1):
            if array[j] < array [j+1] :
                array[j], array[j+1] = array[j+1], array[j]
    print (array)

else:
    print ("Error choose 'a' or 'd'!")