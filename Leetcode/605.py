# https://leetcode.com/problems/can-place-flowers/?envType=study-plan-v2&envId=leetcode-75

f = [0,0,1,0,1]
f.insert(0,0)
f.append(0)
n = 1
for i in range(1, len(f)-1):
    l = i - 1
    r = i + 1
    if f[i] == 0 and l >= 0 and r < len(f):
        if f[l] == 0 and f[r] == 0:
            f[i] = 1
            n -= 1
print(n<=0)
