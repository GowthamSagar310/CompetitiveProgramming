c = 0 
for _ in range(int(input())):
    c += 1 if sum(list(map(int, input().split()))) > 1 else 0
print(c)