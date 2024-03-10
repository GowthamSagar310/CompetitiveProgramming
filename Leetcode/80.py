
nums = [0,0,1,1,1,1,2,3,3]
def solve(nums):
    l,r = 0,0
    while r < len(nums):
        count = 1
        while r < len(nums)-1 and nums[r] == nums[r+1]:
            r += 1
            count += 1
        for i in range(min(2, count)):
            nums[l] = nums[r]
            l += 1
        r += 1

print(solve(nums), nums)