# undirected graph. cycle detection. 


# at some starting node, if you are branching out and then branching in on to the same node, then there is a cycle.
# 1--2 is not cycle
# 1--2 is a cycle
# \3/

# how do you actually know there a branch out happened somewhere in the graph and now a branching in happened ? 

#  1 -- 2 -- 4 -- 5
#                 |
#       6 -- 7 -- 8 
# you cannot start from 1 and 6 simultaneously. 

# the catch here is, you can start only from one node. 
# the branching out happens at some node (but a single node).
# there are no two separate place which start at some time, and meet. 

n, e = list(map(int, input().split()))
adj = [[] for _ in range(n)]

for _ in range(e):
    u,v = list(map(int, input().split()))
    adj[u].append(v)
    adj[v].append(u)

for i,row in enumerate(adj): print(i, row)

visited = [0 for _ in range(n)]

def bfs(node, adj, visited):
    queue = [(node, -1)]
    visited[node] = 1
    while queue:
        node, parent = queue[0]
        for n in adj[node]:
            if visited[n] != 1:
                visited[n] = 1
                queue.append((n, node))
            elif n != parent:
                # somehow i ended up in this place, while still starting from some single node. 
                # but the node that i am gng to is not my parent. 
                return True
        queue.pop(0) 
    return False 

def solve():
    for node in range(n):
        if visited[node] != 1:
            # return bfs(node, adj, visited) is not checking for other nodes. 
            if (bfs(node, adj, visited)): return True
    return False 

print(solve())

