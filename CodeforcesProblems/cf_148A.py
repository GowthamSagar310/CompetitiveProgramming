k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())

arr = [k,l,m,n]
c = 0
for i in range(1, d+1):
    for j in arr:
        if i % j == 0:
            c +=1
            break
print(c)