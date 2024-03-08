n, m = list(map(int, input().split()))
adj = [[] for _ in range(n+1)]
for _ in range(m):
    u,v = list(map(int, input().split()))
    adj[u].append(v)

# this wont work for graphs with cycles.
# dfs 
def toposort(adj,n,m):
    def dfs(node, adj, visited, stack):
        visited[node] = 1
        for nn in adj[node]:
            if visited[nn] != 1:
                dfs(nn, adj, visited, stack)
        stack.append(node)

    stack = []
    visited = [0 for _ in range(n)]
    for i in range(n):
        if visited[i] != 1:
            dfs(i, adj, visited, stack)
    return stack[::-1]


# khan's algorithm 
# this is if nodes are numbered from 1 
def khan_toposort(n,m,adj):
    indegree = [0] * (n+1)
    for i in range(n+1):
        for nn in adj[i]:
            indegree[nn] += 1
    queue = []
    for i in range(n+1):
        if indegree[i] == 0:
            queue.append(i)

    topo = []
    while queue:
        node = queue[0]
        topo.append(node)
        for nn in adj[node]:
            indegree[nn] -= 1
            if indegree[nn] == 0:
                queue.append(nn)
        queue.pop(0)
    return topo

print(khan_toposort(n,m,adj))