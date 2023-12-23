n, m = list(map(int, input().split()))

def is_prime(x):
    for j in range(2, x):
        if x % j == 0:
            return False
    return True

def f(n,m):
    for i in range(n+1, m+1):
        if is_prime(i):
            if i == m:
                return True
            else:
                return False
    return False

print("YES" if f(n,m) else "NO")