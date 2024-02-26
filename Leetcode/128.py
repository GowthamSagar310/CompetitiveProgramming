arr = [100,4,200,1,3,2]
m = {k:1 for k in arr}
longest_till_now = 0
for num in arr:
    count = 0
    if num-1 not in m:
        count += 1
        temp = num + 1
        while temp in m:
            count += 1
            temp += 1
        longest_till_now = max(longest_till_now, count)
print(longest_till_now)




    