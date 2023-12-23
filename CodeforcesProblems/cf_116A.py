max_till_now = -float("inf")
current_cap = 0
for _ in range(int(input())):
    exits, enters = list(map(int, input().split()))
    current_cap += enters - exits
    max_till_now = max(max_till_now, current_cap)
print(max_till_now)