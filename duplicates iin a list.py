arr = [1, 5, 3, 7, 3, 4, 5, 7, 6]

print("Duplicate: ");

for i in range(0, len(arr)):
    for j in range(i + 1, len(arr)):
        if (arr[i] == arr[j]):
            print(arr[j]);