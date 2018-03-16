def merge_sort(arr):
    if len(arr) == 1:
        return arr
    else:
        result = []
        l1 = merge_sort(arr[0: int(len(arr)/2)])
        l2 = merge_sort(arr[int(len(arr)/2): len(arr)])
        i, j = 0, 0
        while True:
            if l1[i] <= l2[j]:
                result.append(l1[i])
                i += 1
            else:
                result.append(l2[j])
                j += 1
            if i == len(l1):
                while j < len(l2):
                    result.append(l2[j])
                    j += 1
                break
            if j == len(l2):
                while i < len(l1):
                    result.append(l1[i])
                    i += 1
                break
        return result

print(merge_sort([9, 4, 7, 1, 2, 5, 11, 3, 6, 8, 5, 9]))

