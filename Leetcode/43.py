# https://leetcode.com/problems/multiply-strings/description/


s1 = "12"
s2 = "26"

def construct_num(str):
    res = 0
    for i in range(len(str)):
        num = ord(str[i]) - ord("0")
        res = 10 * res + num
    return res 

print(str(construct_num(s1)*(construct_num(s2))))