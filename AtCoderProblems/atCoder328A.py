n,x = list(map(int,input().split()))
arr = list(map(int,input().split()))
print(sum([i for i in arr if i <= x]))