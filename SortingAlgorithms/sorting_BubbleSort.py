n = int(input())
l = list(map(int, input().split()))

for i in range(n-1, 0, -1):
    swapped = False
    for j in range(i):
        if l[j] > l[j+1]:
            swapped = True
            l[j], l[j+1] = l[j+1], l[j]
    if not swapped: break

print(l)
    
