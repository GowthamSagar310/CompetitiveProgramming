n = int(input())
arr = list(map(int, input().split()))

left = 0
right = n - 1

while left < right:
    mid = (left + right) // 2
    print(arr[left], arr[mid], arr[right])
    if arr[mid] > arr[left] and arr[mid] > arr[right]:
        left = mid + 1
    else:
        right = mid - 1
