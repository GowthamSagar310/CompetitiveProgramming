n = int(input())

# TLE 
# from collections import Counter
# print(len(Counter(list(map(int, input().split()))).keys()))

# set O(n * logn) --> constant factor is too high 
# TLE 
# import sys
# print(len(sorted(list(map(int, sys.stdin.readline().split())))

# sorting  O(n * logn) --> constant factor is not too high
# best solution
l = sorted(list(map(int, input().split())))
prev = l[0]
count = 1
for i in range(1,n):
    if l[i] != prev:
        prev = l[i]
        count+=1
print(count)
