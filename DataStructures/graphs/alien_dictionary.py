# https://www.codingninjas.com/studio/problems/alien-dictionary_630423

k = 5
dictionary = ["adced", "adcecac", "acabe", "dcac", "dceceacc"]
n = len(dictionary)
adj = [[] for _ in range(k)]

for i in range(n-1):
    s1 = dictionary[i]
    s2 = dictionary[i+1]
    ptr = 0 
    while ptr < min(len(s1), len(s2)):
        if s1[ptr] != s2[ptr]:
            adj[ord(s1[ptr])-ord("a")].append(ord(s2[ptr])-ord("a"))
            break 
        ptr += 1

def toposort(k, adj):

    indegree = [0 for _ in range(k)]
    for i in range(n):
        for nn in adj[i]:
            indegree[nn] += 1

    queue = []
    for i in range(k):
        if indegree[i] == 0:
            queue.append(i)

    ans = []
    while queue:
        node = queue.pop(0)
        ans.append(node)
        for nn in adj[node]:
            indegree[nn] -= 1
            if indegree[nn] == 0:
                queue.append(nn)
    
    for i in range(len(ans)):
        ans[i] = chr(ans[i] + ord("a"))

    print(ans)

toposort(k, adj)