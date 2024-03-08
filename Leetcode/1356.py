# https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/?envType=daily-question&envId=2024-03-07

arr = [1024,512,256,128,64,32,16,8,4,2,1]

def count_ones(num):
    count = 0
    while num > 0:
        num = num & (num-1)
        count += 1
    return count 

print([x[0] for x in sorted([(val, ones) for val, ones in zip(arr, list(map(count_ones, arr)))], key=lambda x: (x[1], x[0]))])

