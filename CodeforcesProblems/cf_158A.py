n,k = list(map(int,input().split()))
arr = list(map(int,input().split()))
c = 0 
for i in range(len(arr)):
    if arr[i] > 0 and arr[i] >= arr[k-1]:
        c += 1
print(c)