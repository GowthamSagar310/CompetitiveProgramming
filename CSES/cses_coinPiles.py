for _ in range(int(input())):
    a,b = list(map(int,input().split()))
    if (max(a,b) <= 2 * min(a,b) and (a+b)%3==0):
        print("YES")
    else:
        print("NO")