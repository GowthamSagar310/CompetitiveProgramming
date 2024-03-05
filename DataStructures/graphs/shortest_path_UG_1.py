n = 8
m = 10
edges =[[1,0],[2,1],[0,3],[3,7],[3,4],[7,4],[7,6],[4,5],[4,6],[6,5]]
src=0


adj = [[] for _ in range(n)]
for edge in edges:
    u,v = edge 
    adj[u].append(v)
    adj[v].append(u)

distance = [float("inf") for _ in range(n)]
distance[src] = 0
queue = [src]

while queue:
    node = queue.pop(0)
    for nn in adj[node]:
        if distance[node] + 1 < distance[nn]:
            distance[nn] = distance[node] + 1
            queue.append(nn) # this is clean trick
            # without using the visited array, we use distance array itself. 
            # if the nn distance is being updated, we previously did not visit the node. 
            # we add it to the array. 
            # we can achieve this using visited array also.
            
print(distance)