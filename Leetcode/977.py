nums = [-5,-4,-3,-2,-1]

# n_values = []
# p_values = []
# for i in nums:
#     if i < 0:
#         n_values.append(i**2)
#     else:
#         p_values.append(i**2)
# lp = 0
# rn = len(n_values)-1
# ans = []
# while lp < len(p_values) and rn >= 0:
#     if p_values[lp] <= n_values[rn]:
#         ans.append(p_values[lp])
#         lp += 1
#     else:
#         ans.append(n_values[rn])
#         rn -= 1

# while lp < len(p_values):
#     ans.append(p_values[lp])
#     lp += 1

# while rn >= 0:
#     ans.append(n_values[rn])
#     rn -= 1

# print(ans)

# must be done using two pointer approach

res = []
l, r = 0, len(nums)-1
while l <= r:
    if abs(nums[l]) < abs(nums[r]):
        res.append(nums[r]*nums[r])
        r -= 1
    else:
        res.append(nums[l] * nums[l])
        l += 1
print(res[::-1])