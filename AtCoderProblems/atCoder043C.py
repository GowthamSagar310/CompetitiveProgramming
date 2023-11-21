import math
n = int(input())
arr = list(map(int, input().split()))
s = round(sum(arr) / n)
cost = 0
for i in arr:
    cost += (s-i) ** 2
print(cost)