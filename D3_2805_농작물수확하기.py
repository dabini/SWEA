T = int(input())

for t in range(T):
    N = int(input())

    field = [[0]*N for _ in range(N)]

    for i in range(N):
        field[i] = list(map(int, input()))

    total = 0
    for y in range(N):
            for x in range(abs(y - N // 2), N-abs(y - N // 2) ):
                total += field[y][x]

    print("#{} {}".format(t+1, total))
