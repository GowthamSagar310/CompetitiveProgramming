# https://leetcode.com/problems/3sum-closest/description/

nums = [-1, 2, 1, -4]
target = 1


def solve(nums, target):
    nums.sort()
    min_target = float("inf")
    ans = target
    for i in range(len(nums)-2):
        l = i + 1
        r = len(nums)-1
        while l < r: 
            s = nums[l] + nums[r] + nums[i]
            if s == target:
                return target
            elif s > target:
                r -= 1
            else:
                l += 1
            if abs(s-target) < min_target:
                min_target = abs(s-target)
                ans = s 
    return ans

print(solve(nums, target))