class BinaryHeap(list):
    def __init__(self, arr):
        super(BinaryHeap, self).__init__(arr)
        self.heap_size = len(self)


def parent(i):
    return int((i-1)/2)


def left(i):
    return 2*i+1


def right(i):
    return 2*(i+1)

"""
Ensure the property of max-heap
Input: array A and index i
At this time we assume left tree and right tree are max-heap
Max-heapify makes A[i] go down in max-heap
"""


def max_heapify(arr, i):
    l = left(i)
    r = right(i)
    if l < arr.heap_size and arr[l] > arr[i]:
        largest = l
    else:
        largest = i
    if r < arr.heap_size and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, largest)


def build_max_heap(arr):
    for i in reversed(range(int(len(arr)/2))):
        max_heapify(arr, i)


def heapsort(arr):
    build_max_heap(arr)
    for i in range(len(arr)-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        arr.heap_size -= 1
        max_heapify(arr, 0)


A = BinaryHeap([16, 14, 10, 8, 7, 9, 3, 2, 4, 1])
heapsort(A)
print(A)
