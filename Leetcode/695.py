grid = [
    [0,0,1,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,1,1,0,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,1,1,0,0,1,0,1,0,0],
    [0,1,0,0,1,1,0,0,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,1,1,0,0,0,0]
]

def bfs(n, m, row, col, grid, visited):
    queue = [(row, col)]
    visited[row][col] = 1
    count = 0
    while queue:
        row, col = queue[0]
        count += 1
        row_ops, col_ops = [+1, -1, 0, 0], [0, 0, +1, -1]
        for rop, cop in zip(row_ops, col_ops):
            r = row + rop 
            c = col + cop 
            if r >= 0 and r < n and c >= 0 and c < m and visited[r][c] != 1:
                visited[r][c] = 1
                if grid[r][c] == 1:
                    queue.append((r,c))
        queue.pop(0)
    return count

def solve(grid):
    n,m = len(grid), len(grid[0])
    points = []
    for row in range(n):
        for col in range(m):
            if grid[row][col] == 1:
                points.append((row,col))
    visited = [[0 for _ in range(m)] for _ in range(n)]
    maxi = 0
    for point in points:
        row, col = point
        if visited[row][col] != 1:
            maxi = max(maxi, bfs(n, m, row, col, grid, visited))
    return maxi

print(solve(grid))