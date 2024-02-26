# https://leetcode.com/problems/container-with-most-water/
# container with most water. 


arr = [0,0,1,0,1]
# max_area = 0
# for i in range(len(arr)):
#     if arr[i] != 0:
#         for j in range(len(arr)-1, i, -1):
#             area = min(arr[i], arr[j]) * (j-i)
#             if area > max_area:
#                 max_area = area 
# print(max_area)

arr = [1,8,6,2,5,4,8,3,7]
res = 0
l, r = 0, len(arr)-1
while l < r:
    area = min(arr[l], arr[r]) * (r-l)
    res = max(res, area)
    if arr[l] > arr[r]: r -= 1
    else: l += 1
print(res)