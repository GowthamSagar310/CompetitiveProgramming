from queue import PriorityQueue

n, m, src = list(map(int, input().split()))

adj = [[] for _ in range(n)]
for _ in range(m):
    u,v,wt = list(map(int, input().split()))
    adj[u].append((v,wt))
    adj[v].append((u,wt))

pq = PriorityQueue()
pq.put((0, src))
distance = [float("inf") for _ in range(n)]
distance[src] = 0
while not pq.empty():
    d, node = pq.get()
    for item in adj[node]:
        nn, wt = item 
        if d + wt < distance[nn]:
            distance[nn] = d + wt 
            pq.put((d+wt, nn))
            
print(distance)