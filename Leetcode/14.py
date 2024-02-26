# longest common prefix
#  https://leetcode.com/problems/longest-common-prefix/description/

strs = ["a"]
strs = ["ab", "a"]
# strs = ["flower","flow","flight"]

def solve(strs):
    res = ""
    for l in range(len(strs[0])):
        temp = strs[0][l]
        for j in range(1, len(strs)):
            if l >= len(strs[j]): return res 
            if temp != strs[j][l]: return res 
        res += temp
    return res

print(solve(strs))