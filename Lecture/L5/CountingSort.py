def countingsort(arr, k):
    c = []
    b = arr.copy()
    for i in range(0, k):
        c.append(0)
    for j in range(0, len(arr)):
        c[arr[j]] = c[arr[j]] + 1
    for i in range(1, k):
        c[i] = c[i] + c[i-1]
    for j in range(len(arr)-1, -1, -1):
        b[c[arr[j]]-1] = arr[j]
        c[arr[j]] = c[arr[j]] - 1
    return b

print(countingsort([0, 1, 2, 5, 4, 7, 9, 5, 3, 6, 8], 10))

