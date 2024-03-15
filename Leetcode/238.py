nums = [1,2,3,4]

# left_mul = []
# right_mul = []
# for i in range(len(nums)):
#     if i == 0:
#         left_mul.append(1)
#         continue 
#     left_mul.append(left_mul[-1] * nums[i-1])
# print(left_mul)
# for i in range(len(nums)-1,-1,-1):
#     if i == len(nums)-1:
#         right_mul.append(1)
#         continue
#     right_mul.append(right_mul[-1] * nums[i+1])
# print(right_mul)
# l = 0
# r = len(nums)-1
# ans = []
# while r >= 0 and l < len(nums):
#     ans.append((left_mul[l] * right_mul[r]))
#     l += 1
#     r -= 1
# print(ans)

# time O(n) and space O(1) solution 
def solve(nums):
    res = [1] * len(nums)
    prefix = 1 
    for i in range(len(nums)):
        res[i] = prefix # we can override the res, because of initial config. 
        prefix *= nums[i]
    postfix = 1
    for i in range(len(nums)-1, -1, -1):
        res[i] *= postfix # be cautious of this, do not override the res. 
        postfix *= nums[i]
    return res

print(solve(nums))