# https://www.codingninjas.com/studio/problems/flood-fill-_1082141

n, m = list(map(int, input().split()))
x, y, p = list(map(int, input().split()))

image = [
    [7, 1, 1, 1],
    [1, 7, 7, 7],
    [7, 7, 7, 0],
    [7, 7, 7, 4],
    [4, 4, 4, 4]
]

queue = []
queue.append((x,y))

row_ops = [+1, -1, 0, 0]
col_ops = [0, 0, +1, -1]

ic = image[x][y]
while queue:
    row, col = queue[0]
    image[row][col] = p
    for rop,cop in zip(row_ops, col_ops):
        r = row + rop 
        c = col + cop 
        if r >= 0 and r < n and c >= 0 and c < m:
            if image[r][c] == ic:            
                queue.append((r,c))
    queue.pop(0)

for row in image: print(row)