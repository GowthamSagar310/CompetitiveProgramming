# n, m = list(map(int, input().split()))
# arr = [(i,v) for i,v in enumerate(list(map(int, input().split())),1)]
# z = 0
# while arr:
#     if z == len(arr): break
#     if arr[z][1] > m:
#         arr[z] = (arr[z][0], arr[z][1]-m)
#         arr.append(arr[z])
#     z += 1
# print(arr[z-1][0])


# another approach
n, m = list(map(int, input().split()))
arr = list(map(int, input().split()))

max_index = 0 

# for i in range(n):
#     if arr[i] / m 