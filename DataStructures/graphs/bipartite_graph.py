# https://www.codingninjas.com/studio/problems/check-bipartite-graph-_920551


# try to colour, until its not possible. 

graph = [
    [1,3],
    [0,2],
    [1,3],
    [0,2]
]

def color(node, adj, visited):
    visited[node] = 0   
    queue = []
    queue.append(node)
    while queue:
        node = queue[0]
        for n in adj[node]:
            if visited[n] == -1:
                visited[n] = int(not visited[node])
                queue.append(n)
            elif visited[n] == visited[node]:
                return False 
        queue.pop(0)
    return True 

def solve(graph):
    visited = [-1 for _ in range(len(graph))]
    for node in range(len(graph)):
        if visited[node] == -1:
            if not color(node, graph, visited):
                return False 
    return True 

print(solve(graph))