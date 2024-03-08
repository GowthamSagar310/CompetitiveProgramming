# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/submissions/1195474760/?envType=daily-question&envId=2024-03-06

def solve(nums, target):

    def first(nums, target):
        first = -1
        l = 0
        r = len(nums)-1
        while l <= r:
            mid = (l+r) // 2
            if nums[mid] == target:
                first = mid 
                r = mid-1
            elif nums[mid] > target:
                r = mid-1
            else:
                l = mid+1
        return first
    
    def last(nums, target):
        last = -1
        l = 0
        r = len(nums)-1
        while l <= r:
            mid = (l+r) // 2
            if nums[mid] == target:
                last = mid 
                l = mid + 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return last 
    
    return [first(nums, target), last(nums, target)]
