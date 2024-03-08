# https://www.codingninjas.com/studio/problems/detect-cycle-in-a-directed-graph-_920545

n, m = 3, 3
edges = [
    [0,1],
    [1,2],
    [0,2],
]

adj = [[] for _ in range(n)]
for i in range(m):
    u,v = edges[i]
    adj[u].append(v)

for i, row in enumerate(adj): print(i, row)



def dfs(node, adj, visited, pathvisited):
    visited[node] = 1 
    pathvisited[node] = 1
    for nn in adj[node]:
        if visited[nn] != 1:
            if dfs(nn, adj, visited, pathvisited): return True 
            pathvisited[nn] = 0
        elif visited[nn] == 1 and pathvisited[nn] == 1:
            return True  
    return False 

def solve(adj):
    visited = [0 for _ in range(n)]
    pathvisited = [0 for _ in range(n)]
    for node in range(1, n):
        if visited[node] != 1:
            if dfs(node, adj, visited, pathvisited): 
                return True
    return False 

print(solve(adj))