x,y = -1,-1
for i in range(5):
    row = list(map(int, input().split()))
    if x == -1 and y == -1:
        for j in range(5):
            if row[j] == 1:
                x,y = i+1, j+1

print(abs(x-3) + abs(y-3))