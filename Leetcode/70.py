def recur(n, dp):
    if n <= 1:
        return 1
    if dp[n] != -1: return dp[n]
    dp[n-1] = recur(n-1, dp)
    dp[n-2] = recur(n-2, dp)
    return dp[n-1] + dp[n-2]

n = 5
dp = [-1] * (n+1)

print(recur(n, dp))