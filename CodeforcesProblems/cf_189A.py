n, a, b, c = list(map(int, input().split()))
lengths = sorted(list(set([a,b,c])), reverse=True)

# def recursive_travel(current_value, depth, max_value):
#     if current_value == 0:
#         return depth
#     if current_value < lengths[0]:
#         return 0
#     for m in lengths:
#         if m <= current_value:
#             max_value = max(max_value, recursive_travel(current_value-m, depth+1, max_value))
#     return max_value 

# print(recursive_travel(n, 0, 0))

results = []
def stack_travel(n):
    stack = []
    stack.append((n,0))
    max_depth = 0
    while stack:
        print(stack)
        current_value, depth = stack.pop()
        if current_value == 0:
            max_depth = max(max_depth, depth)
        if current_value > 0:
            for m in lengths:
                if m <= current_value and current_value >= 0:
                    if current_value-m not in results:
                        stack.append((current_value-m, 1+depth))
                        results.append(current_value-m)
    return max_depth

print(stack_travel(n))





