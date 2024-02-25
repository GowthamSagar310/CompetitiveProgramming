# https://www.codingninjas.com/studio/problems/rotting-oranges_701655

n, m = list(map(int, input().split()))

grid = [
    [2,1,1],
    [1,1,0],
    [1,1,1]
]

def bfs(grid):
    total_oranges = 0
    queue = []
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] != 0: total_oranges += 1
            if grid[row][col] == 2: queue.append((row, col))
    row_ops = [+1, -1, 0, 0]
    col_ops = [0, 0, +1, -1]
    orange_count = 0
    time = 0
    while queue:
        s = len(queue)
        orange_count += s 
        # batch wise 
        while s > 0: 
            row, col = queue[0]
            for rop, cop in zip(row_ops, col_ops):
                r = row + rop 
                c = col + cop 
                if (r >= 0 and r < n) and (c >= 0 and c < m):
                    if grid[r][c] == 1:
                        grid[r][c] = 2
                        queue.append((r,c))
            queue.pop(0)
            s -= 1
        if queue: time += 1 

        # only if there are more rottens to visit, time is going to increase.
        # example [2,1,1][1,1,0][1,1,1]. grid[2][2] is the last rotten orange, visiting last rotten tomato should not change the time.
    return time if total_oranges == orange_count else -1

print(bfs(grid))    


