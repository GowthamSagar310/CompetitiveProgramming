arr = []

l = 0
r = len(arr)-1
res = float("inf")
while l <= r:
    mid = (l + r) // 2
    if arr[l] <= arr[mid]:
        res = min(res ,arr[l])
        l = mid + 1
    else:
        res = min(res, arr[mid])
        r = mid - 1
print(res)