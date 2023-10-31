n = int(input())
if n <= 3:
    if n == 1:
        print("1")
    else: 
        print("NO SOLUTION")
else:
    la = []
    lb = []
    for i in range(1, n+1):
        if i % 2 == 0: la.append(i)
        else: lb.append(i)
    l = la + lb 
    print(" ".join(list(map(str, l))))
