def binary_search(arr, low, high, x):
    if low > high:
        return -1
    else:
        mid = int((low + high) / 2)
        if x > arr[mid]:
            return binary_search(arr, mid + 1, high, x)
        elif x < arr[mid]:
            return binary_search(arr, low, mid - 1, x)
        else:
            return mid

print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 0, 8, 9))