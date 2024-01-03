from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    map = {} # value : index
    for i in range(len(nums)):
        if (target-nums[i]) in map:
            return [map.get(target-nums[i]), i]
        else:
            map[nums[i]] = i

arr = list(map(int, input().split()))
target = int(input())
print(twoSum(arr, target))



