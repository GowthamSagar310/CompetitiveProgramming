n, target = list(map(int, input().split()))
arr = list(map(int, input().split()))

left = 0
right = n-1
first_occurence_index = -1
while left <= right:
    mid = (left + right) // 2
    if arr[mid] >= target:
        first_occurence_index = mid
        right = mid-1
    else:
        left = mid +1 

if first_occurence_index == -1: print (0)
else:
    left = first_occurence_index
    right = n-1
    last_occurence_index = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            last_occurence_index = mid 
            left = mid + 1
        else:
            right = mid - 1
    print (last_occurence_index - first_occurence_index + 1) 