n = int(input())
arr = list(map(int, input().split()))
d = {5:0, 0:0}
for i in arr:
    d[i] += 1
    
if d[5] >= 9:
    if d[0] > 0:
        s = "5" * (9 * (d[5] // 9))
        s += "0" * d[0]
    else:
        s = "-1"
else:
    if d[0] > 0:
        s = "0"
    else:
        s = "-1"

print(s)
