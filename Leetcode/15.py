# https://leetcode.com/problems/3sum/


nums = [-1,0,1,2,-1,-4]

# nums.sort()
# print(nums)
# ans = []
# for i in range(len(nums)):

#     if nums[i] > 0: break
    
#     if i > 0 and nums[i] == nums[i-1]:
#         continue

#     l = i+1
#     r = len(nums)-1
#     while l < r:
#         if nums[l] + nums[r] == -nums[i]:
#             ans.append([nums[l], nums[r], nums[i]])
#             l += 1
#             while nums[l] == nums[l-1] and l < r:
#                 l += 1
#         elif nums[l] + nums[r] < -nums[i]:
#             l += 1
#         else:
#             r -= 1
    
# print(ans)


nums = [-1,-1,0,0,1,1]
def solve(nums):
    if len(nums) < 3: return []
    ans = []
    nums.sort()
    for i in range(len(nums)-2):
        if nums[i] > 0: return ans 
        l = i + 1
        r = len(nums)-1
        if i > 0 and nums[i-1] == nums[i]: continue
        while l < r:
            if nums[i] + nums[l] + nums[r] == 0:
                ans.append([nums[i], nums[l], nums[r]])
                l += 1
                r -= 1
                while nums[l] == nums[l-1] and l < r:
                    l += 1
                while nums[r] == nums[r+1] and l < r:
                    r -= 1
            elif nums[i] + nums[l] + nums[r] > 0:
                r -= 1
            else:
                l += 1
    return ans 
