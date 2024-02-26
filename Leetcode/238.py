nums = [10, 2]
left_mul = []
right_mul = []
for i in range(len(nums)):
    if i == 0:
        left_mul.append(1)
        continue 
    left_mul.append(left_mul[-1] * nums[i-1])
print(left_mul)
for i in range(len(nums)-1,-1,-1):
    if i == len(nums)-1:
        right_mul.append(1)
        continue
    right_mul.append(right_mul[-1] * nums[i+1])
print(right_mul)
l = 0
r = len(nums)-1
ans = []
while r >= 0 and l < len(nums):
    ans.append((left_mul[l] * right_mul[r]))
    l += 1
    r -= 1
print(ans)