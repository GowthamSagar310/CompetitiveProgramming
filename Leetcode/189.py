# https://leetcode.com/problems/rotate-array/?envType=study-plan-v2&envId=top-interview-150

nums = [1,2,3,4,5,6,7]
k = 3

# k %= len(nums)
# can use slicing also.

# repeated work --> slow
# for i in range(k):
#     temp = nums[-1]
#     for i in range(len(nums)-1, 0, -1):
#         nums[i] = nums[i-1]
#     nums[0] = temp
# print(nums)

k %= len(nums)
l,r = 0,len(nums)-1
while l < r:
    nums[l], nums[r] = nums[r], nums[l]
    l += 1
    r -= 1

l,r = 0, k-1

while l < r:
    nums[l], nums[r] = nums[r], nums[l]
    l += 1
    r -= 1

l,r = k, len(nums)-1
while l < r:
    nums[l], nums[r] = nums[r], nums[l]
    l += 1
    r -= 1

print(nums)
