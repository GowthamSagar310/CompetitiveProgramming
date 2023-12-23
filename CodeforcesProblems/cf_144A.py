n = int(input())
arr = list(map(int, input().split()))

min_index, max_index = 0,0 

# min_index < max_index 
# min_index = max_index
# min_index > max_index

for i in range(n):
    if arr[max_index] < arr[i]:
        max_index = i
    if arr[min_index] >= arr[i]:
        min_index = i 

if min_index == max_index or (min_index == n-1 and max_index == 0): 
    print(0)
elif min_index < max_index:
    print( (n-1-min_index) + (max_index-0) - 1)
else:
    print((n-1-min_index) + (max_index-0))
