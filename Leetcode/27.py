# https://leetcode.com/problems/remove-element/description/?envType=study-plan-v2&envId=top-interview-150

nums = [0,1,2,2,3,0,4,2]
val = 2

# stack = []
# for i in range(len(nums)):
#     if nums[i] != val:
#         stack.append(nums[i])

# l = len(stack)
# i = 0
# while stack:
#     nums[i] = stack.pop()
#     i += 1

# print(l)


# vp = 0
# nvp = len(nums)-1
# while vp < nvp:
#     while vp < len(nums) and nums[vp] != val:
#         vp += 1
#     while nvp > 0 and nums[nvp] == val:
#         nvp -= 1
#     if vp < nvp:
#         nums[vp], nums[nvp] = nums[nvp], nums[vp]
#     vp += 1
#     nvp -= 1
# print(len(nums)-nums.count(val))

val_pointer = 0
for i in range(len(nums)):
    if nums[i] != val:
        nums[val_pointer] = nums[i]
        val_pointer += 1
print(nums, val_pointer)