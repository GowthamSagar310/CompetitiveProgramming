# remove duplicates from sorted array

nums = [0,0,1,1,1,2,2,3,3,4]

l = 0
r = 0
count = 1
while l < len(nums) and r < len(nums):
    if nums[l] != nums[r]:
        count += 1
        nums[l+1] = nums[r]
        l += 1
        r += 1
    else:
        r += 1
print(l+1, nums)
