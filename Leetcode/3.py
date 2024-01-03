# def longest(s):
#     max_count = 0
#     index = 0
#     while index < len(s):
#         map = {}
#         count = 0
#         for i in range(index, len(s)):
#             if s[i] not in map:
#                 count += 1
#                 map[s[i]] = map.get(s[i], 0)
#                 max_count = max(max_count, count)
#             else: break
#         index += 1
#     return max_count



# s = input()
# print(longest(s))