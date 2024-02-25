# https://www.codingninjas.com/studio/problems/find-the-number-of-states_1377943

n = 4
roads = [
    [1,1,0,0],
    [1,1,0,0],
    [0,0,1,1],
    [0,0,1,1]
]

# def bfs(row, col, roads, visited):
#     row_ops = [+1, -1, 0, 0]
#     col_ops = [0, 0, +1, -1]
#     queue = [(row, col)]
#     while queue:
#         row, col = queue[0]
#         for row_op, col_op in zip(row_ops, col_ops):
#             r = row + row_op
#             c = col + col_op
#             if r >= 0 and r < len(roads) and c >= 0 and c < len(roads):
#                 if visited[r][c] != 1 and roads[r][c] == 1:
#                     visited[r][c] = 1
#                     queue.append((r, c))    
#         queue = queue[1:]

def bfs(node, adj, visited):
    queue = []
    queue.append(node)
    visited[node] = 1
    while queue:
        node = queue[0]
        for n in adj[node]:
            if visited[n] != 1:
                visited[n] = 1
                queue.append(n)
        queue = queue[1:]
    
visited = [[0 for _ in range(n)] for _ in range(n)]
count = 0

adj = [[] for _ in range(n)]
for row in range(n):
    for col in range(n):
        if roads[row][col] == 1 and row != col:
            adj[row].append(col)
            adj[col].append(row)
for i, row in enumerate(adj): print(i, row)

for node in range(n):
    if visited[node] != 1:
        count += 1
        bfs(node, adj, visited)

print(count)