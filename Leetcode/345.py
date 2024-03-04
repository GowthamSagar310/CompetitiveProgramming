# https://leetcode.com/problems/reverse-vowels-of-a-string/description/?envType=study-plan-v2&envId=leetcode-75

s = "aA"
v = []
vowels = list("aeiouAEIOU")

for i in s:
    if i in vowels:
        v.append(i)

res = ""
j = len(v)-1

for i in range(len(s)):
    if s[i] in vowels:
        res += v[j]
        j -= 1
    else:
        res += s[i]
print(res)
