s = input()
d = {}
d = {l: d.get(l,0) +1 for l in s}
print("CHAT WITH HER!" if len(d.keys())%2==0 else "IGNORE HIM!")