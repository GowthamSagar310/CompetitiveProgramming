# https://leetcode.com/problems/group-anagrams/description/

strs = ["eat", "tea", "ate", "tan", "nat", "bat"]
truth = [False] * len(strs)
ans = []

def get_map(str):
    m = {}
    for s in str:
        m[s] = m.get(s, 0) + 1
    return m 

for i in range(len(strs)):
    temp = []
    if not truth[i]:
        temp.append(strs[i])
        for j in range(i+1, len(strs)):
            if len(strs[i]) != len(strs[j]): continue
            if set(strs[i]) != set(strs[j]): continue
            m1 = get_map(strs[i])
            m2 = get_map(strs[j])
            if m1 == m2:    
                temp.append(strs[j])
                truth[j] = True
    if temp: ans.append(temp)
print(ans)


# better solutions 

# use sorted version of each word as a key in map and appned the original value.
# take values of the map at last. 
# O(avg_len(strings)* log(avg_len(strings)) * number of strings)

# same thing but without sorting, use a count array as a key. 

import collections
strs = ["eat", "tea", "ate", "tan", "nat", "bat"]
m = collections.defaultdict(list)
for s in strs:
    count = [0] * 26
    for c in s:
        count[ord(c)-ord('a')] += 1
    m[tuple(count)].append(s)
print(list(m.values()))