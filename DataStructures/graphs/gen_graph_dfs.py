n, m = list(map(int, input().split()))
adj = [[] for _ in range(n+1)]
for _ in range(m):
    u,v = list(map(int, input().split()))
    adj[u].append(v)
    adj[v].append(u)

for i, row in enumerate(adj): print(i, row)
visited = [0 for _ in range(n+1)]
def dfs(node, visited, adj, path):
    visited[node] = 1
    path.append(node)
    for n in adj[node]:
        if visited[n] != 1:
            dfs(n, visited, adj, path)
    return path 

print(dfs(1, visited, adj, []))


