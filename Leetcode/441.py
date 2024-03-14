# https://leetcode.com/problems/arranging-coins/

def solve(n):
    n = 1
    for i in range(1,n+1):
        if (i * (i + 1)) // 2 > n:
            return i-1
    return n 

