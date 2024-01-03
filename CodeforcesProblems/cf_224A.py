import math 
x, y, z = list(map(int, input().split()))

c = math.sqrt((z * y) // x)
a = (c * x) // y
b = (x // a)

print(int(4 * (a + b + c)))

