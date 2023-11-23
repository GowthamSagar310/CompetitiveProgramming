ld = ["4", "7"]
c = 0
for i in input():
    if i in ld:
        c+=1
print("YES" if str(c) in ld else "NO")