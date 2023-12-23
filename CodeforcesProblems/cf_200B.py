n = int(input())
arr = list(map(int, input().split()))
s = sum(list(map(lambda x: x/100, arr)))
print((s/n)*100)
