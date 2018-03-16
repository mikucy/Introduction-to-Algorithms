def insert_sort(arr):
    for i in range(1, len(arr)):
        if arr[i] <= arr[0]:
            arr.insert(0, arr[i])
            del arr[i+1]
        else:
            for j in range(i-1, -1, -1):
                if arr[i] > arr[j]:
                    arr.insert(j+1, arr[i])
                    del arr[i+1]
                    break
    return arr

print(insert_sort([9, 4, 7, 1, 2, 5, 11, 3, 6, 8, 5]))

