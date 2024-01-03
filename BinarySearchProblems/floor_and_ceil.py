n, target = list(map(int, input().split()))
arr = list(map(int, input().split()))

left = 0
right = n-1

floor_val = -1
ceil_val = -1

while left <= right: 
    mid = (left + right) // 2
    if arr[mid] == target:
        floor_val, ceil_val = target, target
        break
    elif arr[mid] > target:
        ceil_val = arr[mid]
        right = mid-1
    else:
        floor_val = arr[mid]
        left = mid + 1
print(floor_val, ceil_val)
