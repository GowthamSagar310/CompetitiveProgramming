n = int(input())
l = list(map(int, input().split()))

count = 0
for i in range(n-1):
    if l[i] > l[i+1]:
        diff = l[i]-l[i+1]
        count += diff
        l[i+1] += diff

print(count)