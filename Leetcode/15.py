# https://leetcode.com/problems/3sum/


nums = [-1,0,1,2,-1,-4]
nums.sort()
print(nums)
ans = []
for i in range(len(nums)):

    if nums[i] > 0: break
    
    if i > 0 and nums[i] == nums[i-1]:
        continue

    l = i+1
    r = len(nums)-1
    while l < r:
        if nums[l] + nums[r] == -nums[i]:
            ans.append([nums[l], nums[r], nums[i]])
            l += 1
            while nums[l] == nums[l-1] and l < r:
                l += 1
        elif nums[l] + nums[r] < -nums[i]:
            l += 1
        else:
            r -= 1
    
print(ans)

