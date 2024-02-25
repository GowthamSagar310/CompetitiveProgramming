# https://www.codingninjas.com/studio/problems/matrix-traps_8365440


n, m = list(map(int, input().split()))
matrix = [
    [1,1,0,1],
    [0,1,0,1],
    [1,0,1,0],
    [1,0,1,1],
    [0,1,0,1]
]

def bfs(matrix):
    total_zeros = 0
    queue = []
    zeros_count = 0 

    n = len(matrix)
    m = len(matrix[0])
    visited = [[0 for _ in range(m)] for _ in range(n)]

    for row in range(n):
        for col in range(m):
            if matrix[row][col] == 0: total_zeros += 1 
            if row == 0 or row == n-1 or col == 0 or col == m-1:
                if matrix[row][col] == 0:
                    visited[row][col] = 1
                    zeros_count += 1
                    queue.append((row, col))

    while queue:
        row, col = queue[0]
        visited[row][col] = 1
        row_ops, col_ops = [+1, -1, 0, 0], [0, 0, +1, -1]
        for rop, cop in zip(row_ops, col_ops):
            r = row + rop 
            c = col + cop 
            if r >= 0 and r < n and c >= 0 and c < m and visited[r][c] != 1:
                visited[r][c] = 1
                if matrix[r][c] == 0:
                    queue.append((r,c))
                    zeros_count += 1

        queue.pop(0)

    return total_zeros - zeros_count


print(bfs(matrix))


