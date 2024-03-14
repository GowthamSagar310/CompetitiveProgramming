# https://leetcode.com/problems/boats-to-save-people/description/

# each boat can carry only two people
# is this not two sum

people = [1,2,3]
limit = 3
# 1 (1,2)

# people = [3,2,2,1]
# limit = 3
# # 3 (3) (2, 1) (2) 

# people = [3,5,3,4]
# limit = 5
# # (3) (3) (5) (4)

# 3 3 4 5
# 1 2 5 4

def solve(nums, k):
    nums.sort()
    l,r = 0,len(nums)-1
    count = 0
    while l <= r:
        if nums[l] + nums[r] <= k:
            l += 1
            r -= 1
        else:
            r -= 1
        count += 1
    return count 

print(solve(people, limit))