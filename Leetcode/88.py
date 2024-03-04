# https://leetcode.com/problems/merge-sorted-array/?envType=study-plan-v2&envId=top-interview-150

nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
m, n = 3, 3 

l1 = 0
l2 = 0 

ans = []
while l1 < m and l2 < n:
    if nums1[l1] <= nums2[l2]:
        ans.append(nums1[l1])
        l1 += 1
    else:
        ans.append(nums2[l2]) 
        l2 += 1

while l1 < m:
    ans.append(nums1[l1])
    l1 += 1

while l2 < n:
    ans.append(nums2[l2])
    l2 += 1

for i in range(len(ans)): 
    nums1[i] = ans[i]

print(nums1)
