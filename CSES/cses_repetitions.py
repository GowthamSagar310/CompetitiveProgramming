s = input()
max_count = 0
count = 0
for i in range(len(s)-1):
    if s[i] == s[i+1]:
        count += 1
    else:
        count = 0
    # if count > max_count: 
    #     max_count = count 
    max_count = max(max_count, count)
    
print(max_count + 1)
