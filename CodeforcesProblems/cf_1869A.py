# did not solve yet

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    xor_arr = [0] * (n+1)

    s = 0
    for i in range(1, n+1):
        xor_arr[i] = xor_arr[i-1] ^ arr[i-1]
        s += arr[i-1]
    if s == 0:
        print(0)
    elif xor_arr[-1] == 0:
        print(1)
        print(1, n, sep=" ")
    else:
        if n % 2 == 0:
            print(2)
            print(1, n)
            print(1, n)
        else:
            # order does not matter
            # need even number of same numbers and one zero 
            for i in range(n-1):
                print(arr[i], arr[i+1])