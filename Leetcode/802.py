# https://leetcode.com/problems/find-eventual-safe-states/description/

graph = [[],[0,2,3,4],[3],[4],[]]

n = len(graph)
out_degree = [0] * n
for i in range(n):
    out_degree[i] += len(graph[i])
print(out_degree)

queue = []
for i in range(n):
    if out_degree[i] == 0:
        queue.append(i)
