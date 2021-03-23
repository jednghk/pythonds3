"""
idea:
1. have quicksort function which takes in start, end and array (start and end allows for recursive call later)
2. have partition function which returns the index of the split point, allowing qs to be called on left and right list
3. base case of recursive call: start < end, guarantees that there are more than one element in list

review:
Version 1 of code doesn't work as the base case should be in the outer function(qsort), not scoped function (partition)
- Why does quicksort change the list in place without an equal operator?
"""


def quick_sort(arr, start, end):
    if start < end:
        pIndex = partition(arr, start, end)
        arr = quick_sort(arr, start, pIndex - 1)
        arr = quick_sort(arr, pIndex + 1, end)
    return arr

def partition(arr, start, end):
    """takes end as pivot, sets pIndex to first elem, if pIndex < pivot, swap with elem at pI and pI+=1, else pass"""
    pIndex = start
    pivot = arr[end]
    for i in range(start, end):#start + 1?
        if arr[i] < pivot:
            arr[pIndex], arr[i] = arr[i], arr[pIndex]
            pIndex += 1
    arr[end], arr[pIndex] = arr[pIndex], arr[end]
    return pIndex

print(partition([2,7,1,6,8,5,3,4], 0, 7))
print(quick_sort([2,7,1,6,8,5,3,4], 0, 7))

"""
def partitionV1(arr, start, end):
    takes end as pivot, sets pIndex to first elem, if pIndex < pivot, swap with elem at pI and pI+=1, else pass
    pIndex = start
    pivot = arr[end]
    if start < end:
        for i in range(start, end):#start + 1?
            if arr[i] < pivot:
                arr[pIndex], arr[i] = arr[i], arr[pIndex]
                pIndex += 1
        arr[end], arr[pIndex] = arr[pIndex], arr[end]
    return pIndex
"""