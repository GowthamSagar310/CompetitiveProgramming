# https://leetcode.com/problems/course-schedule/description/

n = 2 
pre_reqs = [[1,0]]

adj = [[] for _ in range(n)]
for edge in pre_reqs:
    v,u = edge
    adj[u].append(u)
print(adj)

def khans_topo(n, adj):

    indegree = [0 for _ in range(n)]
    for i in range(n):
        for nn in adj[i]:
            indegree[nn] += 1
    
    queue = []
    for i in range(n):
        if indegree[i] == 0:
            queue.append(i)
    count = 0    
    while queue:
        node = queue[0]
        count += 1
        for nn in adj[node]:
            indegree[nn] -= 1
            if indegree[nn] == 0:
                queue.append(nn)
        queue.pop(0)
    return count == n
