# https://leetcode.com/problems/majority-element/description/?envType=study-plan-v2&envId=top-interview-150
nums = [3,2,3]
def solve(nums):
    res, count = 0,0
    for n in nums:
        if count == 0:
            res = n 
        count += (1 if res == n else -1)
    return res 

print(solve(nums))