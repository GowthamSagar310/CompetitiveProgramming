# https://leetcode.com/problems/move-zeroes/?envType=study-plan-v2&envId=leetcode-75

nums = [1,0,1]
l = 0 
for r in range(1, len(nums)):
    if nums[l] == 0:
        if nums[r] != 0:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
    else:
        l += 1
print(nums)