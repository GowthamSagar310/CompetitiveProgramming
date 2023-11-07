n = int(input())
arr = list(map(int, input().split()))

max1 = arr[0] 
max2 = -float('inf')

min1 = arr[0] 
min2 = float('inf')

for i in arr:
    if i > max1:
        max2 = max1 
        max1 = i 
    elif i != max1 and i > max2:
        max2 = i

    if i < min1: 
        min2 = min1
        min1 = i 
    elif i != min1 and i < min2:
        min2 = i

    
print(max1, min1, max2, min2)
