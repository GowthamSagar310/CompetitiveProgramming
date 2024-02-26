# the question that we need to ask is  
# what is the max_product till now, regardless of current elemenet ? 

nums = [-2, -2, -1]


res = max(nums)
max_till_now, min_till_now = 1,1 

for i in nums:
    if i == 0:
        max_till_now, min_till_now = 1,1
        continue
    
    temp = i * max_till_now
    max_till_now = max(i * max_till_now, i * min_till_now, i)
    min_till_now = min(temp, i * min_till_now, i)
    res = max(res, max_till_now, min_till_now)

print(res)