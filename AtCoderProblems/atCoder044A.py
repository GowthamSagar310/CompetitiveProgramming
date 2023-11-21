n = int(input())
k = int(input())
x = int(input())
y = int(input())

print(((n) * x) if n <=k else ((k) * x + (n-k) * y))    