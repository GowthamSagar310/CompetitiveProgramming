s = input()
uc = 0
for i in s:
    if i.isupper(): uc+=1
lc = len(s) - uc
print(s.upper() if uc > lc else s.lower())

