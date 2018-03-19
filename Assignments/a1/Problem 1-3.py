def unimodal_search(arr):
    low = 0
    high = len(arr) - 1
    while high > low:
        mid = int((high+low)/2)
        if arr[mid] > arr[mid-1]:
            low = mid + 1
        if arr[mid] < arr[mid+1]:
            high = mid - 1
    return arr[low]


print(unimodal_search([1, 2, 3, 7, 8, 9, 8, 6, 5, 4]))