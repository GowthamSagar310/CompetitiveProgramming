# https://www.codingninjas.com/studio/problems/distinct-islands_630460


grid = [
    [1,1,0,0,0],
    [1,1,0,0,0],
    [0,0,0,0,0],
    [0,0,0,1,1],
    [0,0,0,1,1]
]


def bfs(row, col, grid, visited):
    n = len(grid)
    m = len(grid[0])
    l = [(0,0)]
    base_r, base_c = row, col
    queue = []
    queue.append((row, col))
    visited[row][col] = 1
    while queue:
        row, col = queue[0]
        row_ops, col_ops = [+1, -1, 0, 0], [0, 0, +1, -1]
        for rop, cop in zip(row_ops, col_ops):
            r = row + rop 
            c = col + cop 
            if r >= 0 and r < n and c >= 0 and c < m and visited[r][c] != 1:
                visited[r][c] = 1
                if grid[r][c] == 1:
                    l.append((base_r-r,base_c-c))
                    queue.append((r,c))
        queue.pop(0)
    print(tuple(l))
    return tuple(l)

def solve(grid):
    n = len(grid)
    m = len(grid[0])
    visited = [[0 for _ in range(m)] for _ in range(n)]
    count = 0
    superset = set()
    for row in range(n):
        for col in range(m):
            if grid[row][col] == 1 and visited[row][col] != 1:
                visited[row][col] = 1
                count += 1
                s = bfs(row, col, grid, visited)
                superset.add(s)
    return len(superset)

print(solve(grid))