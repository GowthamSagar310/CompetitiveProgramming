
def solve(nums, target):
    nums.sort()
    for i in range(len(nums)-2): # we need three numbers atleast
        l = i + 1
        r = len(nums)-1
        while l < r: 
            if nums[l] + nums[r] + nums[i] == target:
                return True 
            elif nums[l] + nums[r] + nums[i] > target:
                r -= 1
            else:
                l += 1
    return False



nums = [1,-1,0]
target = -1
print(solve(nums, target))