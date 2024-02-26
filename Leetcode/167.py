# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

arr = [2,3,4]
target = 6

def solve(arr):
    l = 0
    r = len(arr)-1
    while l < r:
        if arr[l] + arr[r] == target:
            return [l+1, r+1]
        elif arr[l] + arr[r] < target:
            l += 1
        else:
            r -= 1

print(solve(arr))