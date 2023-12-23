n = int(input())
arr = list(map(int, input().split()))

min_index, max_index = 0,0 

for  i in range(n):
    if arr[i] >= arr[max_index]:
        max_index = i
    if arr[i] <= arr[min_index]:
        min_index = i

if min_index == max_index:
    print(0)
else:
    ans = (max_index - 0) + (n - min_index - 1) 
    print(ans if min_index > max_index else ans-1)