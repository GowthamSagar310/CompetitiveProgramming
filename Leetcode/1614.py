# https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/description/

# same can be done with stack
def solve(s):
    count = 0    
    m = 0
    for i in s:
        if i == "(":
            count += 1
            m = max(m, count)
        elif i == ")":
            if count > 0: 
                count -= 1
    return m

