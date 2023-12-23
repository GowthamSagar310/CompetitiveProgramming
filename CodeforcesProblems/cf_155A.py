n = int(input())
arr = list(map(int, input().split()))
c = 0
for i in range(1, n):
    broke = False
    for j in range(i):
        if arr[i] < arr[j]: 
            broke = True
        else: 
            broke = False
            break
    if broke: 
        c += 1
    else:
        for j in range(i):
            if arr[i] > arr[j]:
                broke = True
            else: 
                broke = False
                break
        if broke : c += 1

print(c)