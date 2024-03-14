# https://leetcode.com/problems/valid-palindrome-ii/description/


s = "deeeec"

# recursive solution
def solve(l, r, c, s):
    if l > r : return True
    if s[l] == s[r]: 
        return solve(l+1, r-1, c, s)
    if s[l] != s[r]: 
        if c == 0:
            return solve(l, r-1, 1, s) or solve(l+1, r, 1, s)
        else:
            return False 

print(solve(0, len(s)-1, 0,s))

def iterative_solution(s):
    l, r = 0, len(s)-1
    while l < r:
        if s[l] != s[r]:
            skip_l, skip_r = s[l+1:r+1], s[l:r]
            return (skip_l == skip_l[::-1]) or (skip_r == skip_r[::-1])
        l += 1
        r -= 1  
    return True 
print(iterative_solution(s))