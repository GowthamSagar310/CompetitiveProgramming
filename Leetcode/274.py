# https://leetcode.com/problems/h-index/description/?envType=study-plan-v2&envId=top-interview-150

citations = [11,15]

# sorting takes atleast n*log(n)
# there is a better solution 
# def solve(citations):
#     citations.sort()
#     n = len(citations)
#     for i,value in enumerate(citations):
#         if n-i <= value:
#             return (n-i)
#     return 0

def solve(citations):
    n = len(citations)
    temp = [0 for _ in range(n+1)]
    for i,value in enumerate(citations):
        if value > n: temp[n] += 1
        else: temp[value] += 1
    total = 0
    for i in range(n, -1, -1):
        total += temp[i]
        if total >= i:
            return i
        
print(solve(citations))