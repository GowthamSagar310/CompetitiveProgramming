# https://leetcode.com/problems/sort-colors/description/

nums = [0,1,0]

def solve(nums):
    low, mid, high = 0,0,len(nums)-1
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            mid += 1
            low += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
    return nums

print(solve(nums))