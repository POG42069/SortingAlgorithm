def merge(arr, low, mid, high):
    L = []
    R = [] 
    n_1, n_2 = mid - low + 1, high - mid
    for i in range(n_1):
        L.append(arr[low + i])
    for j in range(n_2):
        R.append(arr[mid + 1 + j]) 
    i, j, k = 0, 0, low   
    while i < n_1 and j < n_2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i < n_1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n_2:
        arr[k] = R[j]
        j += 1
        k += 1

def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2

        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)