# https://leetcode.com/problems/sort-array-by-parity/

nums = [0,1,2]

def solve(nums):
    l = 0
    for r in range(len(nums)):
        if nums[r] % 2 == 0:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
    return nums

print(solve(nums))