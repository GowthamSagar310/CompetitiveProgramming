n,t = list(map(int, input().split()))
q = list(input())

# for i in range(n-1):
#     if q[i] == "B" and q[i+1] == "G":
#         q[i], q[i+1] = q[i+1], q[i]
#     print("".join(q))

for _ in range(t):
    i = 0
    while i < n-1:    
        if q[i] == "B":
            if q[i+1] == "G":
                q[i], q[i+1] = q[i+1], q[i]
                i+=1
        i+=1
print("".join(q))