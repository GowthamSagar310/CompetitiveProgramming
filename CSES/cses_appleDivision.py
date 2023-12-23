n = int(input())
l = list(map(int, input().split()))
a_sum = l[0]
b_sum = l[1]
if n == 1: 
    print(l[0])
elif n == 2: 
    print(abs(l[0]-l[1]))
else:
    for i in range(2, n):
        if a_sum > b_sum: 
            b_sum += l[i]
        else:
            a_sum += l[i]
    print(abs(a_sum - b_sum))
