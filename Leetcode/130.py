grid = [
    ["X","X","X","X"],
    ["X","O","O","X"],
    ["X","X","O","X"],
    ["X","O","X","X"]
]

def bfs(n, m, row, col, grid, visited, dont_change):
    queue = [(row, col)]
    visited[row][col] = 1
    dont_change[row][col] = True 

    while queue:
        row, col = queue[0]
        row_ops, col_ops = [+1, -1, 0, 0], [0, 0, +1, -1]
        for rop, cop in zip(row_ops, col_ops):
            r = row + rop 
            c = col + cop 
            if r >= 0 and r < n and c >= 0 and c < m and visited[r][c] != 1:
                visited[r][c] = 1
                if grid[r][c] == "O":
                    dont_change[r][c] = True
                    queue.append((r,c))
        queue.pop(0)


def solve(grid):
    n, m = len(grid), len(grid[0])
    dont_change = [[False for _ in range(m)] for _ in range(n)]
    points = []
    for row in range(n):
        for col in range(m):
            if grid[row][col] == "X": dont_change[row][col] = True
            if row == 0 or row == n-1 or col == 0 or col == m-1:
                if grid[row][col] == "O":
                        dont_change[row][col] = True
                        points.append((row, col))
    visited = [[0 for _ in range(m)] for _ in range(n)]
    for point in points:
        row, col = point
        if visited[row][col] != 1:
            bfs(n, m, row, col, grid, visited, dont_change)        
        
    for row in range(n):
        for col in range(m):
            if not dont_change[row][col]:
                if grid[row][col] == "O":
                    grid[row][col] = "X"

        
solve(grid)
for row in grid: print(row)