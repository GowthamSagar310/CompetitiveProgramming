# https://leetcode.com/problems/is-subsequence/description/?envType=study-plan-v2&envId=top-interview-150

s = "bb"
t = "baab"


def solve(s, t):
    if len(s) > len(t): return False
    if len(s) == len(t): return s == t
    ls = 0
    lt = -1
    while ls < len(s):
        for i in range(lt+1, len(t)+1):
            if i != len(t) and s[ls] == t[i]:
                lt = i 
                break 
        if i == len(t): return False 
        ls += 1
    return True 

print(solve(s,t))