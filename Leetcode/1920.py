# https://leetcode.com/problems/build-array-from-permutation/

nums =  [0,2,1,5,3,4]
n = len(nums)
for i in range(n):
    nums[i] += n * (nums[nums[i]] % n)
for i in range(n):
    nums[i] //= n 

print(nums)