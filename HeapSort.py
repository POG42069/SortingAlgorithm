def heapify(arr, n, i):
    argmax = i
    low = 2 * i + 1
    high = 2 * i + 2

    if low < n and arr[low] > arr[argmax]:
        argmax = low

    if high < n and arr[high] > arr[argmax]:
        argmax = high

    if argmax != i:
        arr[i], arr[argmax] = arr[argmax], arr[i]
        heapify(arr, n, argmax)

def heap_sort(arr, n):
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
