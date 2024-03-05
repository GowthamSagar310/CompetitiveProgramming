# https://leetcode.com/problems/sum-of-beauty-of-all-substrings/description/


s = "aabcb"
l = len(s)

beauty = 0
for i in range(l):
    d = {}
    for j in range(i,l):
        d[s[j]] = d.get(s[j],0) + 1
        beauty += max(d.values())-min(d.values()) 

print(beauty)