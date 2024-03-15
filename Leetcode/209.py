# https://leetcode.com/problems/minimum-size-subarray-sum/description/?envType=study-plan-v2&envId=top-interview-150

target = 7
nums = [2,3,1,2,4,3]

def solve(nums, target):
    s = 0
    min_size = float("inf")
    l = 0
    r = 0
    while r < len(nums):
        
        while r < len(nums) and s < target:
            s += nums[r]
            r += 1
        while l < len(nums) and s >= target:
            s -= nums[l]
            l += 1
            min_size = min(min_size, r-l+1)
            
    return 0 if min_size >= float("inf") else min_size

print(solve(nums, target))