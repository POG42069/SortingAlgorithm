def merge(arr, low, mid, high):
    L = arr[low:mid + 1]
    R = arr[mid + 1:high + 1]
    
    i, j, k = 0, 0, low
    
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
        
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1
        
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1

def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)