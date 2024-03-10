# https://leetcode.com/problems/merge-sorted-array/?envType=study-plan-v2&envId=top-interview-150

nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
m, n = 3, 3 

# l1 = 0
# l2 = 0 

# ans = []
# while l1 < m and l2 < n:
#     if nums1[l1] <= nums2[l2]:
#         ans.append(nums1[l1])
#         l1 += 1
#     else:
#         ans.append(nums2[l2]) 
#         l2 += 1

# while l1 < m:
#     ans.append(nums1[l1])
#     l1 += 1

# while l2 < n:
#     ans.append(nums2[l2])
#     l2 += 1

# for i in range(len(ans)): 
#     nums1[i] = ans[i]

# print(nums1)

last = m+n-1
while m > 0 and n > 0:
    if nums1[m-1] > nums2[n-1]:
        nums1[last] = nums1[m-1]
        m -= 1
    else:
        nums1[last] = nums2[n-1]
        n -= 1
    last -= 1
while n > 0:
    nums1[last] = nums2[n-1]
    n -=1
    last -=1         

print(nums1)