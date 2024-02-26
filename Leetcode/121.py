# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

prices = [1,6]
next_greater = 0
max_diff = 0
for i in range(len(prices)-1, -1, -1):
    if prices[i] > next_greater:
        next_greater = prices[i]
    max_diff = max(max_diff, next_greater - prices[i])
print(max_diff)