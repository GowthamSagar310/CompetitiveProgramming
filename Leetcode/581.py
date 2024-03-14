# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/description/

nums = [1,2,3,3,3]

def solve(nums):

    l, r = 0, len(nums)-1
    while l+1 < len(nums) and nums[l] <= nums[l+1]: l += 1
    while r-1 >= 0 and nums[r-1] <= nums[r]: r -= 1

    if l == len(nums)-1: return 0
    maximum, minimum = max(nums[l:r+1]), min(nums[l:r+1])
    

    while l-1 >= 0 and nums[l-1] > minimum: l -= 1
    while r+1 <= len(nums)-1 and nums[r+1] < maximum: r += 1

    return r - l + 1

print(solve(nums))