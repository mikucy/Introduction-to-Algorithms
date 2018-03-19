def binary_insert_sort(arr):
    for i in range(1, len(arr)):
        idx = binary_insert(arr[0: i], arr[i])
        arr.insert(idx, arr[i])
        del arr[i+1]
    return arr


def binary_insert(arr, key):
    low = 0
    high = len(arr) - 1
    while high >= low:
        mid = int((low+high)/2)
        if key == arr[mid]:
            return mid
        elif key > arr[mid]:
            low = mid + 1
            if low > high:
                return mid + 1
        else:
            high = mid - 1
            if high < low:
                return mid

print(binary_insert_sort([5, 1, 3, 2, 7, 9, 4, 6, 8, 5]))
