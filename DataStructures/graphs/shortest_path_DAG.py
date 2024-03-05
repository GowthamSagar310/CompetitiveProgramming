n = 7
m= 8
edges =[[0,4,2],[0,5,3],[5,4,1],[4,6,3],[4,2,1],[6,1,2],[2,3,3],[1,3,1]]

adj = [[] for _ in range(n)]
for edge in edges:
    u,v,wt = edge 
    adj[u].append((v,wt))

def toposort(adj):
    k = len(adj)
    indegree = [0 for _ in range(k)]
    for i in range(k):
        for nn in adj[i]:
            indegree[nn[0]] += 1
    
    queue = []
    for i in range(k):
        if indegree[i] == 0:
            queue.append(i)

    ans = []
    while queue:
        node = queue.pop(0)
        ans.append(node)
        for nn in adj[node]:
            indegree[nn[0]] -= 1
            if indegree[nn[0]] == 0:
                queue.append(nn[0])
    return ans

ans = toposort(adj)

distance = [float("inf") for i in range(n)]
distance[0] = 0

while ans:
    node = ans.pop(0)
    for nn in adj[node]:
        v,wt = nn 
        if distance[node] + wt < distance[v]:
            distance[v] = distance[node] + wt 
print(distance)        
