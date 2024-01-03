n, target = list(map(int, input().split()))
arr = list(map(int, input().split()))

left = 0
right = n-1
ans = -1

# this is a slight variation of lower_bound
# we might be tempted to think this is lower_bound
# but lower_bound is arr[index] >= target 
# here it is arr[index] == target
# but then again, this is not same as first_true index

# while left <= right:
#     mid = (left + right) // 2
#     if arr[mid] == target: # set ans only when equal
#         ans = mid
#         right = mid-1
#     elif arr[mid] > target:
#         right = mid-1
#     else:
#         left = mid+1
# print(ans)

# first_occurence
while left <= right:
    mid = (left + right) // 2
    if arr[mid] >= target:
        ans = mid
        right = mid-1
    else:
        left = mid +1 
print(ans)

# last_occurence
left = 0
right = n-1
ans = -1
while left <= right:
    mid = (left + right) // 2
    if arr[mid] <= target:
        ans = mid 
        left = mid + 1
    else:
        right = mid - 1
print(ans)
