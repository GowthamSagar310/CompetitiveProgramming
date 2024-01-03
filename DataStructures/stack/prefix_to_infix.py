
def prefix_to_infix(exp):
    
    stack = []

    # read from reverse
    for i in exp[::-1]:
        if "a" <= i <= "z" or "A" <= i <= "Z" or "0" <= i <= "9":
            stack.append(i)
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            stack.append("(" + op1 + i + op2 + ")")

    return "".join(stack)

s = input()
print(prefix_to_infix(s))