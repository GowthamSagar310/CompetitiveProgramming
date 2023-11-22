c = 0
for _ in range(int(input())):
    op = input()
    if ("++") in op:
        c+=1
    else:
        c-=1
print(c)