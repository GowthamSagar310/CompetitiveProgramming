# https://leetcode.com/problems/course-schedule-ii/

n = 2
pre_reqs = [[1,0]]

adj = [[] for _ in range(n)]
for edge in pre_reqs:
    u,v = edge 
    adj[v].append(u)

indegree = [0] * n 
for i in range(n):
    for nn in adj[i]:
        indegree[nn] += 1

queue = []
for i in range(n):
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

print(topo if len(topo)==n else [])