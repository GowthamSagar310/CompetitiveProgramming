# https://www.geeksforgeeks.org/problems/geek-onacci-number/0?category=
    
t = int(input())

def recur(n, arr):
    if n == 1: return arr[0]
    if n == 2: return arr[1]
    if n == 3: return arr[2]
    return recur(n-1, arr) + recur(n-2, arr) + recur(n-3, arr)
    
for _ in range(t):
    a,b,c,n = list(map(int, input().split()))
    print(recur(n, [a,b,c]))
    