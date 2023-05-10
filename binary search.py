array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
key = int(input("input number: "))
def binarysearch(key, array, min, max):
    mid = min + (max - min) // 2
    if (array[mid] < key):
        binarysearch(key, array, mid + 1, max)
        print(mid)
    elif (array[mid] > key):
        binarysearch(key, array, mid - 1)
        print(mid)
    else:
        print(mid)
