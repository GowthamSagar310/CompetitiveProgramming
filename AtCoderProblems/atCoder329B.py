n = int(input())
arr = list(map(int, input().split()))

# find second largest 

max1 = arr[0]
max2 = -9999 # will be in between -100 to +100

for i in range(len(arr)):
    if arr[i] > max1:
        max2 = max1
        max1 = arr[i]
    elif arr[i] > max2 and arr[i] != max1:
        max2 = arr[i]

print(max2)