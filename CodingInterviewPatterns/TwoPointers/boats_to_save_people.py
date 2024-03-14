# remember that there can be only two people in the boat
# and also it deviates a little from the pattern (l <= r)

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