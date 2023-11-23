s1 = input()
s2 = input()

print("".join([str(ord(c1)^ord(c2)) for c1,c2 in zip(s1,s2)]))