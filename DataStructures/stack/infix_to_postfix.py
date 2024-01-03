def precedence(operator):
    if operator == "^": return 3
    if operator == "*" or operator == "/": return 2
    if operator == "+" or operator == "-": return 1
    return -1 

def associativity(operator):
    if operator == "^": return "R"
    return "L"

def infix_to_postfix(exp):
    res = ""
    stack = []

    for i in exp:
        if "a" <= i <= "z" or "A" <= i <= "Z" or "0" <= i <= "9":
            res += i
        elif i == "(":
            stack.append(i)
        elif i == ")":
            while stack and stack[-1] != "(":
                res += stack.pop()
            stack.pop()
        else:
            while stack and stack[-1] != "(" and ((precedence(i) < precedence(stack[-1])) or ((precedence(i) == precedence(stack[-1])) and (associativity(i) == "L"))):
                res += stack.pop()
            stack.append(i)

    while stack:
        res += stack.pop()

    return res

s = input()
print(infix_to_postfix(s))