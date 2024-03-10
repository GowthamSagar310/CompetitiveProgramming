
nums = [5,10,1,5,2]
k = 1

def get_count(num):
    count = 0
    while num > 0:
        num = num & (num-1)
        count += 1
    return count
    
total = 0
for i in range(len(nums)):
    if get_count(i) == k:
        total += nums[i]

print(total)