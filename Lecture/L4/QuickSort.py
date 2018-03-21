def quicksort(arr, p, q):
    if p < q:
        r = partition(arr, p, q)
        quicksort(arr, p, r-1)
        quicksort(arr, r+1, q)


def partition(arr, p, q):
    x = arr[p]
    i = p
    for j in range(p+1, q+1):
        if arr[j] <= x:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[p], arr[i] = arr[i], arr[p]
    return i

arr = [5, 3, 7, 0, 9, 8, 1, 2, 4, 6, 2, 10]
quicksort(arr, 0, len(arr)-1)
print(arr)