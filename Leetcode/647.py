s = "fdsklf"
n = len(s)

res = []
for i in range(n):

    l, r = i, i 
    while l >= 0 and r < n and s[l] == s[r]:
        res.append(s[l:r+1])
        l -= 1
        r += 1
    
    l, r = i, i+1
    while l >= 0 and r < n and s[l] == s[r]:
        res.append(s[l:r+1])
        l -= 1
        r += 1

print(res)

