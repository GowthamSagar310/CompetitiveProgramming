def solve(n):
    k = 1
    s = ((n)*(n+1)) // 2
    if k == s: return k 
    i = 2
    while i <= n:
        k += i
        s -= (i-1)
        if k == s: return i
        i += 1
    return -1

print(solve(8))