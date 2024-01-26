# n = 1 [1]
# n = 2 [1,1]
# n = 3 [1,2,1]
# n = 4 [1,3,3,1] 3c0 3c1 3c2 3c3

# recursive
res = []
def recur(n, res):
    if n == 1: res.append([1]); return
    recur(n-1, res)
    res.append([])
    for i in range(n):
        if i == 0 or i == n-1:
            res[-1].append(1)
        else:
            res[-1].append(res[-2][i] + res[-2][i-1])
recur(5, res)
print(res)

# iterative 
# n = 1 [1]
# n = 2 [1,1]
# n = 3 [1,2,1]
# n = 4 [1,3,3,1] 3c0 3c1 3c2 3c3

# n = 5
# res = []
# for row in range(1, n+1):
#     temp = []
#     for col in range(row):
#         if col == 0 or col == row-1:
#             temp.append(1)
#         else:
#             temp.append(res[-1][col] + res[-1][col-1])
#     res.append(temp)
# print(res)