# https://leetcode.com/problems/rearrange-array-elements-by-sign/description/?envType=daily-question&envId=2024-03-06

nums = [-1,1]
ans = []
p = 1
pp = 0
np = 0
n = len(nums)
    
while len(ans) < n:    
    while pp < n and nums[pp] < 0:
        pp += 1

    while np < n and nums[np] > 0:
        np += 1

    if p:
        ans.append(nums[pp])
        pp += 1
    else:
        ans.append(nums[np])
        np += 1
    p = int(not p)

print(ans)

def solve_2(nums):
    ans = []
    pp = []
    np = []
    for i in nums:
        if i > 0: pp.append(i)
        else: np.append(i)
    for p, n in zip(pp, np):
        ans.append(p)
        ans.append(n)
    return ans 

def solve_3():
    pp, np = 0,1
    ans = [0] * len(nums)
    for i in nums:
        if i > 0:
            ans[pp] = i
            pp += 2
        else:
            ans[np] = i
            np += 2
    return ans 
