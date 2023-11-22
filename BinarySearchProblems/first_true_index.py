arr = [x=="true" for x in input().split()]

low = 0
high = len(arr)-1
ans = -1

# this template is similar to lower_bound
while low <= high:
    mid = (low + high) // 2
    if arr[mid] == True:
        ans = mid
        high = mid-1
    else:
        low = mid+1
print(ans)