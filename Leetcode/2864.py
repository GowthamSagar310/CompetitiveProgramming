# https://leetcode.com/problems/maximum-odd-binary-number/?envType=daily-question&envId=2024-03-01

s = "1011"
n = len(s)
one_count = 0
for i in s:
    if i == "1":
        one_count += 1

res = "1" * (one_count-1) + "0" * (n-(one_count))  + "1" * 1
print(res)

# pointer approach (faster)
s = list(s)
for i in range(len(s)-1, -1, -1):
    if s[i] == "1":
        s[i], s[-1] = s[-1], s[i]
        break 
l = 0
r = i if i != n-1 else i-1 
while l < r:
    if s[l] == "0" and s[r] == "1":
        s[l], s[r] = s[r], s[l]
        l += 1
    elif s[l] == "0" and s[r] == "0":
        r -= 1
    elif s[l] == "1" and s[r] == "0":
        l += 1
        r -= 1
    elif s[l] == "1" and s[r] == "1":
        l += 1

print("".join(s))