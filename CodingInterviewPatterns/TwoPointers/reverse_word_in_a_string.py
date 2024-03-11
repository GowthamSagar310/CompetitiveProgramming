# there are many solutions to this problem. 

# single line solution. 
def solve(s):
    return " ".join(reversed(s.split()))

def solve_2(s):
    n = len(s)
    i = 0
    res = ""
    while i < n:
        # find first non space char. 
        while i < n and s[i] == " ":
            i += 1 
        if i >= n: return res
        # find the next space 
        j = i+1
        while j < n and s[j] != " ":
            j += 1
        if len(res) == 0: res = s[i:j]
        else: res = s[i:j] + " " + res 
        i = j + 1
    return res 