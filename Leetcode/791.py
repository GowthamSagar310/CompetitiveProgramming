# https://leetcode.com/problems/custom-sort-string/description/?envType=daily-question&envId=2024-03-11

from collections import defaultdict
order = "bafg"
s = "abbcd"

res = ""
m = defaultdict(int)
for i in range(len(order)):
    for j in range(len(s)):
        if s[j] == order[i]:
            res += s[j]
            m[s[j]] = 1
for i in range(len(s)):
    if s[i] not in m:
        res += s[i]

print(res)