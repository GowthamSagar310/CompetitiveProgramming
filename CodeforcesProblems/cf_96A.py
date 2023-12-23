s = input()
def f(s):
    one_count = 0
    zero_count = 0
    for i in s:
        if i == "1":
            one_count += 1
            zero_count = 0
        else:
            zero_count += 1
            one_count = 0
        if one_count == 7 or zero_count == 7:
            return True
    return False

print("YES" if f(s) else "NO") 