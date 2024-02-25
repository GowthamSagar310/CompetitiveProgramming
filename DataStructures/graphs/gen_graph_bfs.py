n, m = list(map(int, input().split()))
adj = [[] for _ in range(n+1)]
for _ in range(m):
    u,v = list(map(int, input().split()))
    adj[u].append(v)
    adj[v].append(u)
for i, row in enumerate(adj): print(i, row)

visited = [0 for _ in range(n+1)]
path = []
queue = []
queue.append(1)
visited[1] = 1

while queue:
    node = queue[0]
    path.append(node)
    for n in adj[node]: 
        if visited[n] != 1:
            visited[n] = 1
            queue.append(n)
    queue = queue[1:]
print(path)