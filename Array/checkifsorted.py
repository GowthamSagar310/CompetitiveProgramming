n = int(input())
arr = list(map(int, input().split()))

def checkifsorted(arr, n):
    for i in range(1,n):
        if arr[i] < arr[i-1]:
            return "NO"
    return "YES"

print(checkifsorted(arr,n))