def postfix_to_prefix(exp):
    
    stack = []

    for i in exp:
        if "a" <= i <= "z" or "A" <= i <= "Z" or "0" <= i <= "9":
            stack.append(i) 
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            stack.append(i+ op2 + op1)

    return "".join(stack)

s = input()
print(postfix_to_prefix(s))