# https://leetcode.com/problems/3sum-with-multiplicity/description/

from collections import defaultdict

arr = [0,2,0]
target = 2

def solve(nums, target):
    m = defaultdict(int)
    nums.sort()
    for num in nums: m[num] += 1
    count = 0
    MOD = 1_000_000_0007
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        j = i + 1
        k = len(nums)-1
        while j < k:

            num1, num2, num3 = nums[i], nums[j], nums[k]
            if num1 + num2 + num3 == target:
                if num1 != num2 and num2 != num3:
                    count += ((m[num1] * m[num2] * m[num3])) % MOD
                elif num1 != num2:
                    count += ((m[num1] * (m[num2]) * (m[num2]-1)) // 2) % MOD
                elif num2 != num3:
                    count += ((m[num1] * (m[num1]-1) * m[num3]) // 2) % MOD 
                else:
                    count += ((m[num1] * (m[num1]-1) * (m[num1]-2)) // 6) % MOD 
                    return count 
                j += 1
                k -= 1

                while j > k and nums[j] == nums[j-1]: j += 1
                while j > k and nums[k] == nums[k+1]: k -= 1

            elif num1 + num2 + num3 < target:
                j += 1
                while j > k and nums[j] == nums[j-1]: j += 1
            else:
                k -= 1
                while j > k and nums[k] == nums[k+1]: k -= 1

    return count


print(solve(arr, target))