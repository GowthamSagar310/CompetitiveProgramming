n, target = list(map(int, input().split()))
arr = list(map(int, input().split()))
left = 0
right = len(arr)-1

ans = -1

while left <= right:
    mid = (left + right) // 2
    if arr[mid] == target:
        ans = mid
        break
    elif arr[left] < arr[mid]:
        # left half is sorted
        if arr[left] <= target and target <= arr[mid]:
            right = mid -1
        else:
            left = mid + 1
    else:
        if arr[mid] <= target and target <= arr[right]:
            left = mid + 1
        else:
            right = mid -1

print(ans)
