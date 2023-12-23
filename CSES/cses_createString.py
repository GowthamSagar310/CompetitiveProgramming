s = sorted(list(input()))


def recursive_call(ds, map, ans, s):

    if len(ds) == len(s):
        ans.append("".join(ds.copy()))
        return
    
    already_seen = {k:False for k in s}
    for i in range(len(s)):
        if not map[i] and not already_seen[s[i]]:
            already_seen[s[i]] = True
            map[i] = True
            ds.append(s[i])
            recursive_call(ds, map, ans, s)
            ds.pop()
            map[i] = False
        
    return ans 

ans = recursive_call([], [False] * len(s), [],  s)
print(len(ans))
for permutation in ans:
    print(permutation)