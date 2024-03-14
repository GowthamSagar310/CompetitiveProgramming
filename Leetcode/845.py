# https://leetcode.com/problems/longest-mountain-in-array/description/

nums = [0,1,2,3,4,5,4]

ans = 0
i = 0

while i + 1 < len(nums):

    while i + 1 < len(nums) and nums[i] == nums[i+1]:
        i += 1
    
    increasing = 0 
    decreasing = 0

    while i + 1 < len(nums) and nums[i] < nums[i+1]:
        increasing += 1
        i += 1
    
    while i + 1 < len(nums) and nums[i] > nums[i+1]:
        decreasing += 1
        i += 1
    
    # how many are continously increasing and then decreasing from an index. 
    if increasing > 0 and decreasing > 0:
        ans = max(ans, increasing + decreasing + 1)
    
print(ans)