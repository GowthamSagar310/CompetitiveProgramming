# https://leetcode.com/problems/remove-element/description/?envType=study-plan-v2&envId=top-interview-150

nums = [0,1,2,2,3,0,4,2] 
val = 2

stack = []
for i in range(len(nums)):
    if nums[i] != val:
        stack.append(nums[i])

l = len(stack)
i = 0
while stack:
    nums[i] = stack.pop()
    i += 1

print(l)