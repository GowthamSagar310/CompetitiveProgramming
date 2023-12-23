n = int(input())
l_sum, r_sum = 0,0

for _ in range(n):
    l, r = list(map(int, input().split()))
    l_sum += l 
    r_sum += r 

time = 0 
time += l_sum if l_sum <= n // 2 else (n - l_sum)
time += r_sum if r_sum <= n // 2 else (n - r_sum)

print(time)