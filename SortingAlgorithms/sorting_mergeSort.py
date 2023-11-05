# n = int(input())
# l = list(map(int, input().split()))

# low = 0
# high = n - 1 # inclusive index # last index

# def merge(arr, low, mid, high):
#     temp = []
#     left = low 
#     right = mid+1
#     while low <= mid and right <= high: 
#         if arr[left] < arr[right]:
#             temp.append(arr[left])
#             left += 1
#         else:        
#             temp.append(arr[right])
#             right += 1
    
#     while left <= mid:
#         temp.append(arr[left])
#         left += 1

#     while right <= high: 
#         temp.append(arr[right])
#         right += 1
    
#     # replace arr with temp elements
#     for i in range(low, high+1):
#         arr[i] = temp[i - low]

# def merge_sort(arr, low, high):
#     if low >= high: return 
#     # if low == high : return 
#     # if low >= high : return # just a safety check

#     # if len(arr) > 1 
#     mid = (low+high) // 2
#     merge_sort(arr, low, mid)
#     merge_sort(arr, mid+1, high)
#     merge(arr, low, mid, high)

# merge_sort(l, low, high)
# print(l)


n = int(input())
l = list(map(int, input().split()))

start = 0 
end = n - 1

# all indexes are inclusive


def merge(arr, start, mid, end):

    temp = []
    left = start 
    right = mid + 1

    while left <= mid and right <= end:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1
    
    while left <= mid: 
        temp.append(arr[left])
        left += 1
    
    while right <= end:
        temp.append(arr[right])
        right += 1
    
    # replace arr values with temp values 
    
    # i         --> start, start + 1, ... end 
    # i - start --> 0, 1, ... end - start 
    # end - start essentially means, total number of elements in combined array. 

    # remember end is inclusive
    for i in range(start, end + 1):
        arr[i] = temp[i-start]

def merge_sort(arr, start, end):
    if start >= end: return 
    mid = (start + end) // 2

    # broken down into two arrays 
    merge_sort(arr, start, mid)
    merge_sort(arr, mid+1, end)

    # merge broken arrays 
    merge(arr, start, mid, end)

merge_sort(l, start, end)
print(l)