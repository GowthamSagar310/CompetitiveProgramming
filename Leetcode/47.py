# https://leetcode.com/problems/permutations-ii/

nums = [1,1,2]

def recur(nums, map, ds, ans):
    if len(ds) == len(nums):
        ans.append(ds.copy())
        return 
    for i in range(len(nums)):
        if i > 0 and not map[i-1] and nums[i-1] == nums[i]: continue
        if not map[i]:
            map[i] = True
            ds.append(nums[i])
            recur(nums, map, ds, ans)
            ds.pop()
            map[i] = False 

map = [False] * len(nums)
ans = []
ds = []
nums.sort()
recur(nums, map, ds, ans)
print(ans)
