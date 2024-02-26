# choose three numbers and find the maximum product. 

# there are only 4 combinations in a sorted array   
# last three
# first three
# 1 2 
# 2 1

def maximumProduct(nums):
    nums.sort()

    # c1 
    c1 = 1
    for i in nums[len(nums)-3:]:
        c1 *= i
    
    # c2 
    c2 = 1
    for i in nums[:3]:
        c2 *= i

    # c3 1 2
    c3 = nums[0]
    for i in nums[len(nums)-2:]:
        c3 *= i

    # c4 2 1 
    c4 = 1
    for i in nums[:2]:
        c4 *= i
    c4 *= nums[-1]

    return max(c1,c2,c3,c4)
