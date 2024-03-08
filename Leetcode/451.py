# https://leetcode.com/problems/sort-characters-by-frequency/description/
def solve(s):        
    m = {}
    for i in s:
        m[i] = m.get(i, 0) + 1
    l = sorted([(k,v) for k,v in zip(m.keys(), m.values())], key=lambda x:x[1], reverse=True)
    res = ""
    for i in range(l):
        k,v = l[i]
        res += k*v
    return res