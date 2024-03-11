# https://leetcode.com/problems/shortest-path-in-binary-matrix/description/

from queue import PriorityQueue

grid = [
    [0,0,1],
    [1,1,0],
    [1,1,0]
]

# n = len(grid)
# visited = [[-1 for _ in range(n)] for _ in range(n)]
# new_grid = [[-1 for _ in range(n)] for _ in range(n)]
# node = 0
# zero_count = 0
# for i in range(n):
#     for j in range(n):
#         if grid[i][j] == 0:
#             zero_count += 1
#             new_grid[i][j] = node 
#             node += 1

# adj = [[] for _ in range(zero_count)]
# for i in range(n):
#     for j in range(n):
#         if new_grid[i][j] != -1:
#             visited[i][j] = 1
#             for rop in [-1, 0, +1]:
#                 for cop in [-1, 0, +1]:
#                     r = i + rop
#                     c = j + cop 
#                     if r >= 0 and r < n and c >= 0 and c < n:
#                         if new_grid[r][c] != -1 and visited[r][c] != 1:
#                             adj[new_grid[i][j]].append((new_grid[r][c], 1))
#                             adj[new_grid[r][c]].append((new_grid[i][j], 1))

# for row in new_grid: print(row)
# for i, row in enumerate(adj): print(i, row)

# distance = [float("inf") for _ in range(zero_count)]
# if grid[0][0] == 0: distance[0] = 0

# pq = PriorityQueue()
# pq.put((distance[0], 0))
# while not pq.empty():
#     d, node = pq.get()
#     for item in adj[node]:
#         nn, wt = item 
#         if d + wt < distance[nn]:
#             distance[nn] = d + wt 
#             pq.put((d+wt, nn))

# print(distance)


# better way
# without needing a adjacency matrix. 

def solve(grid):
    
    if grid[0][0] != 0 or grid[-1][-1] != 0: return -1
    n = len(grid)
    if n == 1 and grid[0][0] == 0: return 1 # edge case.
    distance = [[float("inf") for _ in range(n)] for _ in range(n)]
    distance[0][0] = 0 
    # no need of priority queue because of unit weights
    # destination = (n-1, n-1)
            # d  r  c
    queue = [(0, 0, 0)]
    while queue:
        d, r, c = queue.pop(0)
        for rop in [-1,0,1]:
            for cop in [-1,0,1]:
                nr = r + rop 
                nc = c + cop
                if nr >= 0 and nr < n and nc >= 0 and nc < n:
                    if grid[nr][nc] == 0:
                        if d + 1 < distance[nr][nc]:
                            distance[nr][nc] = d+1
                            if nr == n-1 and nc == n-1: return (d+1)+1
                            queue.append((d+1, nr, nc))
    return -1

print(solve(grid))