def prefix_to_postfix(exp):
    
    stack = []

    for i in exp[::-1]:
        if "a" <= i <= "z" or "A" <= i <= "Z" or "0" <= i <= "9":
            stack.append(i)
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            stack.append(op1 + op2 + i)

    return "".join(stack)

s = input()
print(prefix_to_postfix(s))