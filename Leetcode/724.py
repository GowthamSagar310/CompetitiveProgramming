# https://leetcode.com/problems/find-pivot-index/?envType=study-plan-v2&envId=leetcode-75

nums = [1,7,3,6,5,6]

lprefix = [0]
for i in range(1,len(nums)):
    lprefix.append(lprefix[-1] + nums[i-1])

rprefix = [0]
for i in range(len(nums)-2, -1, -1):
    rprefix.append(rprefix[-1] + nums[i+1])
rprefix = rprefix[::-1]

for i in range(len(nums)):
    if lprefix[i] == rprefix[i]:
        print(i)
        break