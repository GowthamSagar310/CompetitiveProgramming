s = input()
d = {}
for l in s:
    if l in d.keys():
        d[l] += 1
    else:
        d[l] = 1

count = 0
no_solution = False
for i in d.values():
    if i % 2 == 1:
        count += 1
    if count > 1: 
        no_solution = True
        break
# print(d)
if no_solution: 
    print("NO SOLUTION")
else:
    p1 = 0
    p2 = len(s)-1
    new_s = ["1"] * len(s)
    k = ""
    for i in d.keys():
        if d[i] % 2 == 0:
            for j in range(d[i]//2):
                new_s[p1] = i
                new_s[p2] = i 
                p1 += 1
                p2 -= 1
        else:
            k = i
    for i in range(p1,p2+1):
        new_s[i] = k
    print("".join(new_s))
    # s = "".join(new_s)
    # print(s==s[::-1])