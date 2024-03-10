# https://leetcode.com/problems/minimum-common-value/description/?envType=daily-question&envId=2024-03-09

nums1 = [1,2,3,5]
nums2 = [4,5]

def solve(nums1, nums2):
    l1 = 0
    l2 = 0
    while l1 < len(nums1) and l2 < len(nums2):
        if nums1[l1] < nums2[l2]:
            l1 += 1
        elif nums1[l1] > nums2[l2]:
            l2 += 1
        else:
            return nums1[l1]
    return -1

print(solve(nums1, nums2))