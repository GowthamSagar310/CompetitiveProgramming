# https://leetcode.com/problems/jump-game/description/

nums = [3,2,1,0,4]
# can_reach = [False] * len(nums)
# can_reach[-1] = True 

# for i in range(len(nums)-2, -1, -1):
#     distance_to_last = (len(nums)-1) - i
#     if (distance_to_last <= nums[i]):
#         can_reach[i] = True
#     else:
#         for j in range(i+1, i+nums[i]+1):
#             if can_reach[j]:
#                 can_reach[i] = True
#                 break 
# print(can_reach[0])

def best_solution(nums):
    end = len(nums)-1
    for i in range(len(nums)-1,-1,-1):
        if i + nums[i] >= end:
            end = i 
    return end == 0
print(best_solution(nums))