n = 4
arr = [["."] * n  for i in range(n)]

# def can_place(row, col, arr):

#     duprow = row 
#     dupcol = col 

#     while row >= 0 and col >= 0:
#         if arr[row][col] == "Q": return False
#         row -= 1
#         col -= 1

#     col = dupcol
#     row = duprow 
#     while col >= 0:
#         if arr[row][col] == "Q": return False
#         col -= 1

#     row = duprow 
#     col = dupcol 
#     while row < n and col >= 0:
#         if arr[row][col] == "Q": return False
#         row += 1
#         col -= 1 
    
#     return True

def can_place(row, col, n, arr):

    duprow = row 
    dupcol = col
    
    # same row 
    if "Q" in arr[row]: return False

    # upper diagonal
    while row > 0 and col > 0:
        row -= 1
        col -= 1
        if arr[row][col] == "Q": return False
    
    row = duprow
    col = dupcol
    # lower diagonal 
    while row < n-1 and col > 0:
        row += 1
        col -= 1
        if arr[row][col] == "Q": return False

    return True

def recur(col, n, arr, res):
    if col == n:
        res.append(["".join(row[:]) for row in arr])
        return
    for row in range(0, n):
        if (can_place(row, col, n, arr)):
            arr[row][col] = "Q"
            recur(col+1, n, arr, res)
            arr[row][col] = "."

res = []
recur(0, n, arr, res)
for ans in res:
    for row in ans:
        print(row)
    print()