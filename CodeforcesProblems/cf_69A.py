x, y, z = 0, 0, 0
for _ in range(int(input())):
    arr = list(map(int, input().split()))
    x += arr[0]
    y += arr[1]
    z += arr[2]

print("YES" if x==0 and y==0 and z==0 else "NO")