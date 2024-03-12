nums = [-4,-1,0,1,5,10]
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