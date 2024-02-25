# adjacency matrix
# undirected graph. 
n, m = list(map(int, input().split()))
adj = [[0 for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    u,v = list(map(int, input().split()))
    adj[u][v] = 1 
    adj[v][u] = 1 # since undirected, u->v edge also means v->u. its not the case in directed graphs
for row in adj: print(row)

# adjacency list 
# undirected graph 
adj = [[] for _ in range(n+1)]
for _ in range(m):
    u,v = list(map(int, input().split()))
    adj[u].append(v)
    adj[v].append(u) # since undirected, u->v edge also means v->u. its not the case in directed graphs
for i,row in enumerate(adj): print(i, row)

# weighted graphs
# in case of adjacency matrix, instead of 1, store the weights 
# in case of adjacency list, store pairs 

adj = [[] for _ in range(n+1)]
for _ in range(m):
    u,v,wt = list(map(int, input().split()))
    adj[u].append((v, wt))
    adj[v].append((u, wt)) # since undirected, u->v edge also means v->u. its not the case in directed graphs
for i,row in enumerate(adj): print(i, row)
