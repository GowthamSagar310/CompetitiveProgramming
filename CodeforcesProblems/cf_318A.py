n, k = list(map(int, input().split()))

num_odd = n // 2 if n % 2 == 0 else (n//2) + 1

if k <= num_odd: 
    # kth odd number 
    print(2 * k - 1)
else:
    # (k - num_odd)th even number 
    print(2 * (k-num_odd))
    