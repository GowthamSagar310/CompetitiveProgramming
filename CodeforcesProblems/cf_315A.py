n = int(input())
# arr = [False]*(1000+1)
# a = []

# for _ in range(n):
#     a_x, b_x = list(map(int, input().split()))
#     a.append(a_x)
#     if a_x != b_x: arr[b_x] = True

# count = 0
# for i in a:
#     if not arr[i]:
#         count += 1
# print(count)

a = []
b = []

for _ in range(n):
    a_x, b_x = list(map(int, input().split()))
    a.append(a_x)
    b.append(b_x)

count = 0
for i in range(n):
    for j in range(n):
        if a[i] == b[j] and i != j:
            count += 1
            break
print(n-count)