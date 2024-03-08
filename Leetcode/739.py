# https://leetcode.com/problems/daily-temperatures/?envType=study-plan-v2&envId=leetcode-75

# temperatures = [89,62,70,58,47,47,46,76,100,70]
# res = [0 for _ in range(len(temperatures))]
# stack = []
# for i, temp in enumerate(temperatures):
#     while stack and temperatures[i] > stack[-1][0]:
#         t, index = stack.pop()
#         res[index] = i-index
#     stack.append((temp, i))
# print(res)

# we can also come from reverse
temperatures = [89,62,70,58,47,47,46,76,100,70]
res = [0 for _ in range(len(temperatures))]
stack = []

for i in range(len(temperatures)-1,-1,-1):
    while stack and temperatures[i] >= stack[-1][0]:
        stack.pop()
    if stack: res[i] = stack[-1][1]-i
    stack.append((temperatures[i], i))
print(res)