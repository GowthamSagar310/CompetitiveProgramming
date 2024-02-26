# https://leetcode.com/problems/valid-parentheses/description/

s = "()(){{}}"

def solve(s):
    map = { "}":"{", ")":"(", "]":"["}
    stack = []
    for c in s:
        if c not in map: # then its a opening bracket
            stack.append(c)
            continue
        if not stack and stack[-1] != map[c]:
            return False
        stack.pop()
    return not stack

def solve2(s):
    stack = []
    for i in range(len(s)):
        if s[i] == "}":
            if stack and stack[-1] != "{":
                stack.pop()
            else: return False
        elif s[i] == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else: return False
        elif s[i] == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else: return False
        else:
            stack.append(s[i])
    
    return len(stack)==0

s = "()[]{}"
print(solve2(s))