nums = [1,2,3,4,5]
k = 1

def solve(nums, k):
    if k == 0: return 0
    l,r = 0,0
    s = 1
    count = 0
    while r < len(nums):
        s *= nums[r]
        r += 1
        while s >= k and l < len(nums):
            s //= nums[l]
            l += 1
        if s > 0 and s < k: count += (r-l)
    return count 

print(solve(nums, k))