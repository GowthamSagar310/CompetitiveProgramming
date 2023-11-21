# from collections import Counter
# s = input()
# c = Counter(s)
# print("Yes" if sum(c.values()) % 2 == 0 else "No")

d = {}
for i in input():
    if i in d: d[i] += 1
    else: d[i] = 1
is_one = False
for i in d.values():
    if i % 2 != 0:
        is_one = True
        break
if is_one: print("No")
else: print("Yes")