# https://leetcode.com/problems/generate-parentheses/

n = 1
ds = ""
ans = []
def recur(index, n, ds, ans, s):
    if index >= n:
        if s == 0:
            ans.append(ds)
            return
        return 
    recur(index+1, n, ds+"(", ans, s+1)
    if s > 0: recur(index+1, n, ds+")", ans, s-1)

recur(1, 2*n, "(", ans, 1)
print(ans)