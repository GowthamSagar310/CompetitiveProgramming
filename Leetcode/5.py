def longestPalindrome(s):
    res = ""
    max_len = 0
    n = len(s)
    for i in range(len(s)):

        # odd 
        l, r = i, i
        while l >= 0 and r < n and s[l] == s[r]:
            if (r-l+1) > max_len:
                max_len = r-l+1
                res = s[l:r+1]
            l -= 1
            r += 1
        # even
        l, r = i, i+1
        while l >= 0 and r < n and s[l] == s[r]:
            if (r-l+1) > max_len:
                max_len = r-l+1
                res = s[l:r+1]
            l -= 1
            r += 1
    return res 
