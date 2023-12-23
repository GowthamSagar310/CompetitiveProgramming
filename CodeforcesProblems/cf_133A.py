s = input()
ins = ["H", "Q", "9"]
flag = False
for l in s:
    if l in ins:
        flag = True
        break
print("YES" if flag else "NO")