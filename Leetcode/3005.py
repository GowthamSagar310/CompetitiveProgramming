nums = [1,2,2,3,1,4,5]
m = {}
for num in nums: m[num] = m.get(num, 0) + 1
count = 0
mm = max(m.values())
for num in m.keys():
    if m[num] == mm:
        count += mm 
print(count)