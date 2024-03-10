# https://leetcode.com/problems/longest-common-subsequence/

t1 = "oxcpqrsvwf"
t2 = "shmtulqrypy"

if len(t1) < len(t2):
    t1,t2 = t2,t1

ml = 0
last = -1
temp = 0

i = 0
while i < len(t2):
    for j in range(last+1, len(t1)+1):
        if j != len(t1) and t2[i] == t1[j]:
            ml += 1
            last = j
            break 
    temp = max(ml, temp)
    if j == len(t1):
        ml = 0
        last = -1
        i -= 1
    i += 1     

print(temp)