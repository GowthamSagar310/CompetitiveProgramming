n = int(input())
l = list(map(int, input().split()))

for i in range(n):
    j = i 
    while j > 0 and l[j] < l[j-1]:
        l[j],l[j-1] = l[j-1],l[j]
        j -= 1
print(l)
