# https://leetcode.com/problems/total-appeal-of-a-string/description/

s = "code"

n = len(s)
dp = {}
total = 0

# not optimized. gives tle

for i in range(n):
    for j in range(i, n+1):
        if s[i:j] in dp:
            total += dp[s[i:j]]
        else:
            total += len(set(s[i:j]))
            if s[i+1:j]:
                dp[s[i+1:j]] = len(set(s[i+1:j]))


print(total)