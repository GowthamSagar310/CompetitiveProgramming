# https://leetcode.com/problems/contains-duplicate-ii/

def solve(nums,k):
    m = {} 
    for i in range(len(nums)):
        if nums[i] in m:
            if abs(m[nums[i]]-i) <= k:
                return True 
        m[nums[i]] = i
    return False 