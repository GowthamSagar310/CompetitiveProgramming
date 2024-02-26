s = input()
def checkValidString(s: str) -> bool:
    stack = []
    star_count = 0
    for i in s:
        if i == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(")")
        elif i == "*": star_count += 1
        elif i == "(": stack.append("(")
    print(stack, star_count)
    if len(stack) == 0: return True
    if len(stack) == star_count: return True
    return False

print(checkValidString(s))