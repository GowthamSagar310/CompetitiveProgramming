# a = list(map(int, input()))
# b = list(map(int, input()))

# # make sure a is always bigger 
# if len(b) > len(a):
#     a, b = b, a
#     b = [0] * (len(a)-len(b)) + b
# elif len(b) < len(a):
#     b = [0] * (len(a)-len(b)) + b

# carry = 0
# ans = []
# for i in range(len(a)-1, -1, -1):
#     if a[i] + b[i] == 2:
#         if carry:
#             ans.append(1)
#             carry = 1 
#         else:
#             ans.append(0)
#             carry = 1
#     if a[i] + b[i] == 1:
#         if carry:
#             ans.append(0)
#             carry = 1
#         else:
#             ans.append(1)
#     if a[i] + b[i] == 0:
#         if carry: 
#             ans.append(1)
#             carry = 0
#         else:
#             ans.append(0)
# if carry: ans.append(1)
# for i in range(len(ans)-1, -1, -1):
#     print(ans[i], end='')


# even better smaller code 

a = input()
b = input()

a, b = a[::-1], b[::-1]
res = ""
carry = 0
for i in range(max(len(a), len(b))):
    digit1 = ord(a[i]) - ord("0") if i < len(a) else 0
    digit2 = ord(b[i]) - ord("0") if i < len(b) else 0 
    total = digit1 + digit2 + carry 
    carry = total // 2  
    res += str(total % 2)
if carry: res += str(1)
print(res[::-1])