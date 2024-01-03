n = int(input())
arr = list(map(int, input().split()))

min_diff = 1000 
index_1 = 0
index_2 = 1
i = 0
for _ in range(n):
    if i == n - 1: 
        if min_diff > abs(arr[-1]- arr[0]):
            index1 = n-1
            index2 = 0
            min_diff = abs(arr[-1] - arr[0])
    else:
        if min_diff > abs(arr[i] - arr[i+1]):
            index1 = i
            index2 = i + 1
            min_diff = abs(arr[i] - arr[i+1])
    i += 1

print(index1+1, index2+1)