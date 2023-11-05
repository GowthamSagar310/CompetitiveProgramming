n = int(input())
l = list(map(int, input().split()))

def get_pivot_index(arr, start, end):
    pivot = arr[start]
    left = start 
    right = end 

    while (left < right):  # when they dont cross each other 
    
        # find element which is greater than pivot 
        # until i find an element greater than pivot, i ll search
        while (arr[left] <= pivot) and left <= end-1: 
            left += 1
        
        # find element which is smaller than pivot
        # until i find an element less than
        while (arr[right] > pivot) and right >= start + 1:
            right -= 1
        
        # if they dont cross each other 
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]

    arr[start], arr[right] = arr[right], arr[start]
    return right



def quick_sort(arr, start, end):
    if start >= end: return
    pivot_index = get_pivot_index(arr, start, end)
    quick_sort(arr, start, pivot_index-1)
    quick_sort(arr, pivot_index + 1, end)

quick_sort(l, 0, n-1)
print(l)