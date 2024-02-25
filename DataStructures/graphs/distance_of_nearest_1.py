# https://www.codingninjas.com/studio/problems/distance-of-nearest-cell-having-1-in-a-binary-matrix_1169913

n, m = list(map(int, input().split()))

matrix = [
    [1, 0, 0, 0],
    [1, 0, 0, 0]
]

# def bfs(row, col, matrix, visited):
#     queue = [(row, col)]
#     visited[row][col] = 1
#     distance = 0
#     while queue:
#         s = len(queue)
#         for _ in range(s):
#             row, col = queue[0]
#             visited[row][col] = 1
#             row_ops = [+1, -1, 0, 0]
#             col_ops = [0, 0, +1, -1]
#             for rop, cop in zip(row_ops, col_ops):
#                 r = row + rop 
#                 c = col + cop 
#                 if r >= 0 and r < len(matrix) and c >= 0 and c < len(matrix[0]):
#                     if matrix[r][c] == 0 and visited[r][c] != 1:
#                         visited[r][c] = 1
#                         queue.append((r,c))
#                     elif matrix[r][c] == 1:
#                         return distance + 1
#             queue.pop(0)
#         distance += 1
#     return distance


# d = [[0 for _ in range(m)] for _ in range(n)]
# for row in range(n):
#     for col in range(m):
#         if matrix[row][col] == 0:
#             visited = [[0 for _ in range(m)] for _ in range(n)]
#             d[row][col] = bfs(row, col, matrix, visited)

# for row in d: print(row)

# one more way to do this 


queue = []
visited = [[0 for _ in range(m)] for _ in range(n)]
for row in range(n):
    for col in range(m):
        if matrix[row][col] == 1:
            queue.append((row, col, 0))
            visited[row][col] = 1

distance = [[0 for _ in range(m)] for _ in range(n)]
while queue:
    row, col, steps = queue[0]
    visited[row][col] = 1
    distance[row][col] = steps
    row_ops = [+1, -1, 0, 0]
    col_ops = [0, 0, +1, -1]
    for rop, cop in zip(row_ops, col_ops):
        r = row + rop 
        c = col + cop 
        if r >= 0 and r < n and c >= 0 and c < m and visited[r][c] != 1:
            visited[r][c] = 1
            queue.append((r,c,steps+1))
    queue.pop(0)

for row in distance: print(row)