i_state = [[1,1,1],[1,1,1],[1,1,1]]
press = []
f_state = [[1,1,1], [1,1,1], [1,1,1]]

def f(n):
    n = int(n)
    return 0 if n % 2 == 0 else 1

for _ in range(3):
    press.append(list(map(f, input().split())))

for i in range(3):
    for j in range(3):
        if press[i][j] == 1:
            f_state[i][j] = (1 - f_state[i][j])
            if i > 0:
                f_state[i-1][j] = (1 - f_state[i-1][j])
            if i < 2:
                f_state[i+1][j] = (1 - f_state[i+1][j])
            if j > 0: 
                f_state[i][j-1] = (1 - f_state[i][j-1])
            if j < 2:
                f_state[i][j+1] = (1 - f_state[i][j+1])

for i in range(3):
    for j in range(3):
        print(f_state[i][j], end='')
    print()

