# https://www.codingninjas.com/studio/problems/replace-%E2%80%98o%E2%80%99-with-%E2%80%98x%E2%80%99_630517

n, m = list(map(int, input().split()))

grid = [
    ["X", "X", "O", "X", "X", "X"],
    ["X", "X", "O", "X", "O", "X"],
    ["X", "X", "X", "O", "O", "X"],
    ["X", "O", "X", "X", "X", "X"],
    ["O", "X", "O", "O", "X", "X"],
    ["X", "X", "X", "X", "O", "X"],
]

def bfs(grid):

    n = len(grid)
    m = len(grid[0])

    dont_change = [[False for _ in range(m)] for _ in range(n)]
    for row in range(n):
        for col in range(m):
            if grid[row][col] == "X":
                dont_change[row][col] = True

    queue = []
    visited = [[0 for _ in range(m)] for _ in range(n)]

    for row in range(n):
        for col in range(m):
            if row == 0 or row == n-1 or col == 0 or col == m-1:
                if (grid[row][col] == "O"):
                    visited[row][col] = 1
                    queue.append((row, col))
    while queue:
        row, col = queue[0]
        visited[row][col] = 1
        dont_change[row][col] = True
        row_ops = [+1, -1, 0, 0]
        col_ops = [0, 0, +1, -1]

        for rop, cop in zip(row_ops, col_ops):
            r = row + rop 
            c = col + cop 
            if r >= 0 and r < n and c >= 0 and c < m and visited[r][c] != 1 and grid[r][c] == "O":
                visited[r][c] = 1
                dont_change[r][c] = True
                queue.append((r, c))
        
        queue.pop(0)
    
    for row in range(n):
        for col in range(m):
            if not dont_change[row][col]:
                grid[row][col] = "X"

bfs(grid)
for row in grid: print(row)
