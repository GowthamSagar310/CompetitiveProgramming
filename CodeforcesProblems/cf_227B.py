n = int(input())
arr = list(map(int, input().split()))
qs = int(input())
queries = list(map(int, input().split()))

index = [0] * 100001
for i in range(1,n+1):
    index[arr[i-1]] = i

fc, bc = 0,0
for q in queries:
    fc += index[q]
    bc += n - index[q] + 1
print(" ".join(list(map(str, [fc,bc]))))
                   