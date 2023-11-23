s = input()
stack = []
i = 0

while i < len(s):
    if s[i] == ".": stack.append("0")
    elif s[i] == "-" and s[i+1] == "-": 
        stack.append("2")
        i+=1
    elif s[i] == "-" and s[i+1] == ".": 
        stack.append("1")
        i+=1
    i+=1
print("".join(stack))