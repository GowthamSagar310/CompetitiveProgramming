n = int(input())
times = [(index, value) for index, value in enumerate(list(map(int, input().split())), 1)]
times.sort(key=lambda x: x[1])

if n == 1: print(1)
else:
    if (times[0][1] == times[1][1]):
        print("Still Rozdil")
    else:
        print(times[0][0])