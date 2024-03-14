# https://leetcode.com/problems/backspace-string-compare/

s = "ab##"
t = "c#d#"

def solve(s,t):
    
    def next_valid_character(str, index):
        backspace = 0
        while index >= 0:
            if backspace == 0 and str[index] != "#":
                break 
            elif str[index] == "#":
                backspace += 1
            else:
                backspace -= 1
            index -= 1
        return index 

    index_s, index_t = len(s)-1, len(t)-1

    while index_s >= 0 or index_t >= 0:
        index_s = next_valid_character(s, index_s)
        index_t = next_valid_character(t, index_t)

        char_s = s[index_s] if index_s >= 0 else ""
        char_t = t[index_t] if index_t >= 0 else ""

        if char_s != char_t:
            return False 

        index_s -= 1
        index_t -= 1

    return True 


print(solve(s,t))