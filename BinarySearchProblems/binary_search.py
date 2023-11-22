n = int(input())
t = int(input())
arr = list(map(int, input().split()))

# this form of binary_search only works if arr is sorted in asc.
# observe that we are discard the current element. 
def binary_search(arr, n, t):
    left = 0
    right = n-1
    while left <= right: 
        mid = (left + right) // 2
        if arr[mid] == t:
            return mid
        elif arr[mid] < t:
            left = mid + 1
        else:
            right = mid - 1
    return -1

print(binary_search(arr, n, t))
