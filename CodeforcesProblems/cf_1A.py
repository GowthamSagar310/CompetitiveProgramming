n,m,a = list(map(int, input().split()))
x = ((-n) % a) + n
y = ((-m) % a) + m 
if a == 1: print(n*m)
else:
    print((x//a) * (y//a))