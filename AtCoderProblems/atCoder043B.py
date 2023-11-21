s = input()
stack = []
for l in s:
    if l != "B":
        stack.append(l)
    else:
        if stack:
            stack.pop()
print("".join(stack))