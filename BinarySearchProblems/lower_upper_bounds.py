# naive approach would be O(n).
# as array is sorted, we can try to reduce the search space 
# note that if the target is not present in the array, return index as size of the array.
n,target = list(map(int, input().split()))
arr = list(map(int, input().split()))

left = 0
right = n-1
min_index = n


# lower bound arr[index] >= x
# while left <= right:
#     mid = (left + right) // 2
#     if arr[mid] >= target:
#         min_index = mid
#         right = mid-1
#     else:
#         left = mid+1
# print(min_index)


# upper bound arr[index] > x
while left <= right:
    mid = (left + right) // 2
    if arr[mid] > target:
        min_index = mid 
        right = mid - 1
    else:
        left = mid+1
print(min_index)