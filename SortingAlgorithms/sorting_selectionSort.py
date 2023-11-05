n = int(input())
l = list(map(int, input().split()))

for i in range(n-1):
    minIndex = i 
    for j in range(i+1, n):
        if l[j] < l[minIndex]:
            minIndex = j
    l[i], l[minIndex] = l[minIndex], l[i]

print(l)

