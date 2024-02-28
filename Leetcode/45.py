



nums = [2,3,0,1,4]

def recursion(index, nums, dp):
    if index == len(nums)-1:
        return 0
    if dp[index] != -1: return dp[index]
    m = float("inf") 
    for j in range(1, nums[index]+1):
        if index+j <= len(nums)-1:
            m = min(m, 1+recursion(index+j, nums, dp))
    dp[index] = m
    return dp[index]

dp = [-1 for _ in range(len(nums))]
print(recursion(0, nums, dp))