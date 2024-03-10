# https://leetcode.com/problems/add-strings/

def get_nums(str):
    num = 0
    for i in range(len(str)):
        num = num*10 + (ord(str[i])-ord("0"))
    return num 

print(get_nums("134"))