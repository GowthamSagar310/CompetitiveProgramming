

#  You are given a sorted array arr of distinct values and a target value x. You need to search for the index of the target value in the array.

n,target = list(map(int, input().split()))
arr = list(map(int, input().split()))

left = 0
right = n-1
ans = n
# this is exactly lower bound
while left <= right:
    mid = (left + right) // 2
    if arr[mid] >= target:
        right = mid -1
        ans = mid
    else:
        left = mid+1
print(ans)