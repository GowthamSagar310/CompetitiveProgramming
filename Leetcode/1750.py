s = "cabaabac"

def solve(s):
    l = 0
    r = len(s)-1
    while l < r:
        if s[l] == s[r]:
            while l < r and s[l+1] == s[l]:
                l += 1
            while r > 0 and s[r-1] == s[r]:
                r -= 1
            l += 1
            r -= 1
        else:
            return (r-l+1)
    return max(0, r-l+1)

print(solve(s))