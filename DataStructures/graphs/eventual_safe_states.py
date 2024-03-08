# there are two ways to solve this problem. 
# 1. DFS
# 2. khan's algorithm

n, m = list(map(int, input().split()))

adj = [[] for _ in range(n)]
for _ in range(m):
    u,v = list(map(int, input().split()))
    adj[u].append(v)

# visited = [0 for _ in range(n)]
# pathvisited = [0 for _ in range(n)]
# ans = [0 for _ in range(n)]

# def dfs(node, adj, visited, pathvisited, ans): 
#     visited[node] = 1
#     pathvisited[node] = 1
#     for nn in adj[node]:
#         if visited[nn] != 1:
#             if dfs(nn, adj, visited, pathvisited, ans): 
#                 return True 
#         elif pathvisited[nn] == 1:
#             return True 
#     ans[node] = 1
#     pathvisited[node]= 0
#     return False

# for i  in range(n):
#     if visited[i] != 1:
#         dfs(i, adj, visited, pathvisited, ans)

# for i in range(len(ans)):
#     if ans[i] == 1:
#         print(i, end=" ")

# khan's algorithm 

def solve(adj):

    # terminal node is which has no outgoing edges. 
    # if we can somehow travel back from terminal nodes to others, 
    # and also remove the links from terminal nodes to other
    # and in the process if those nodes indegree becomes zero, there are safe nodes. 
    # to traverse, we need to reverse the graph. 
    
    n = len(adj)
    revadj = [[] for _ in range(n)]
    for i in range(n):
        for nn in adj[i]:
            revadj[nn].append(i)

    indegree = [0 for _ in range(n)]
    for i in range(n):
        for nn in revadj[i]:
            indegree[nn] += 1
    
    queue = []
    for i in range(n):
        if indegree[i] == 0:
            queue.append(i)    

    ans = []
    while queue:
        node = queue.pop(0)
        ans.append(node)
        for nn in revadj[node]:
            indegree[nn] -= 1
            if indegree[nn] == 0:
                queue.append(nn)
    
    return sorted(ans)

print(solve(adj))
    