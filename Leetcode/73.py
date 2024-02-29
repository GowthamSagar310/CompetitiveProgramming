# https://leetcode.com/problems/set-matrix-zeroes/description/

matrix = [
    [0,1,2,0],
    [3,4,5,2],
    [1,3,1,5]
]

n, m = len(matrix), len(matrix[0])

row = [False] * n
col = [False] * m

for r in range(n):
    for c in range(m):
        if matrix[r][c] == 0:
            row[r] = True
            col[c] = True

for r in range(n):
    if row[r]: 
        matrix[r] = [0] * m 

for c in range(m):
    if col[c]:
        for r in range(n):
            matrix[r][c] = 0
        
for row in matrix:
    print(row)