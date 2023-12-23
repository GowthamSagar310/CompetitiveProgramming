n = int(input())
arr = [input().replace(" ","") for _ in range(n)]
d = {}
for i in arr:
    if i not in d: d[i] = 1
    else: d[i] += 1
print(d)
max_config = max(d, key=d.get)
t = 0
for i in range(n):
    config = arr[i]
    for j in range(2):
        if config[j] != max_config[j]:
            t+=1
print(t)