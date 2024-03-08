# https://leetcode.com/problems/first-bad-version/

def isBadVersion(n):
    pass 

def solve(n):
    l = 1
    r = n 
    first = l
    while l <= r:
        mid = (l+r) // 2
        if not isBadVersion(mid):
           l = mid + 1
        else:
            first = mid
            r = mid - 1 
    return first 
