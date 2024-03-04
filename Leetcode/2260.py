# https://leetcode.com/problems/minimum-consecutive-cards-to-pick-up/description/

cards = [1,2,3,4]

l = 0
r = 0

m = {}

n = len(cards)
min_val = float("inf")
while r < n:
    if cards[r] not in m:
        m[cards[r]] = 1
        r += 1
    else:
        min_val = min(min_val, r-l+1)
        del m[cards[l]]
        l += 1
print(min_val if min_val != float("inf") else -1)


