def merge(left, right, arr):
    i = 0
    j = 0
    k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
            k += 1
        else:
            arr[k] = right[j]
            j += 1
            k += 1
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
    return arr


def merge_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        midpoint = len(arr)//2
        l = merge_sort(arr[:midpoint])
        r = merge_sort(arr[midpoint:])
        return merge(l,r,arr)

print(merge_sort([8,2,4,1,6,5,3,7]))