n, e = list(map(int, input().split()))
adj = [[] for _ in range(n+1)]

for _ in range(e):
    u,v = list(map(int, input().split()))
    adj[u].append(v)
    adj[v].append(u)

for i,row in enumerate(adj): print(i, row)

def dfs(node, parent, adj, visited):
    visited[node] = 1
    for n in adj[node]:
        if visited[n] != 1:
            if (dfs(n, node, adj, visited)): return True
        elif n != parent:
            return True
    return False


def solve(visited, adj):
    for i in range(1, n+1):
        if visited[i] != 1:
            if dfs(i, -1, adj, visited): return True
    return False 

visited = [0 for _ in range(n+1)]
print(dfs(1, -1, adj, visited))