# https://leetcode.com/problems/k-diff-pairs-in-an-array/description/


nums = [1,1,1,1,1]
k = 0


def solve(nums, k): 
    l,r = 0,1
    count = 0
    while l < len(nums) and r < len(nums):
        if nums[r] - nums[l] == k:
            count += 1
            r += 1
            l += 1
            while r < len(nums) and nums[r] == nums[r-1]:
                r += 1
        elif nums[r] - nums[l] < k:
            r += 1
        else:
            l += 1
            if l-r == 0: r += 1
    return count 


print(solve(nums,k))