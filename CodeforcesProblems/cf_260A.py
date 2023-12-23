a,b,n = list(map(int, input().split()))

def f(a,b):
    temp = a
    for i in range(0, 10):
        if (a * 10 + i) % b == 0:
            a = a * 10 + i
            break
    return -1 if temp == a else a 

a = f(a,b)
if a == -1:
    print(-1)
else:
    for _ in range(n-1):
        a = a * 10 
    print(a)
