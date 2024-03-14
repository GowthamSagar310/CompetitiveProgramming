# https://leetcode.com/problems/binary-subarrays-with-sum/description/?envType=daily-question&envId=2024-03-14

nums = [1,0,1,0,1] 
goal = 2

def solve(nums, goal):
    if goal < 0: return 0 # there are only 0, 1
    s = 0
    l = 0
    count = 0
    for r in range(len(nums)):
        s += nums[r]
        while s > goal: # by end of this loop, s <= goal 
            s -= nums[l]
            l += 1
        count += (r-l+1) # window size 
    return count 

print((solve(nums, goal) - solve(nums, goal-1)))