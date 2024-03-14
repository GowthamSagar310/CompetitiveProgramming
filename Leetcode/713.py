# https://leetcode.com/problems/subarray-product-less-than-k/description/

nums = [0,1,1]
k = 1


def solve(nums, k):
    if k == 0: return 0
    pass 

print(solve(nums, k))

def subarrays(nums):
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            print(nums[i:j+1])
# subarrays(nums)

def recursive_subarrays(nums, start, end):
    if start >= len(nums) and end >= len(nums): return 
    if end >= len(nums):
        recursive_subarrays(nums, start+1, start+1)
    else:
        print(nums[start:end+1])
        recursive_subarrays(nums,start,end + 1)

def recursive_subarrays_2(nums, start, end):
    if end == len(nums): return 
    if start > end:
        recursive_subarrays_2(nums, 0, end+1)
    else:
        print(nums[start:end+1])
        recursive_subarrays_2(nums, start+1, end)
