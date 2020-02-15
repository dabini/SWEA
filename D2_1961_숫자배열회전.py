T = int(input())

for t in range(T):
    print("#{}".format(t+1))
    N = int(input())

    field = [[0]*N for _ in range(N)]

    for k in range(N):
        field[k] = list(map(str, input().split()))

    out = [[0]*3 for _ in range(N)]

    for y in range(N-1, -1, -1):
        num = ''
        for x in range(N):
            num += field[x][y]
        out[-(y+1)][2] = num


    for y in range(N):
        num = ''
        for x in range(N-1, -1, -1):
            num += field[y][x]
        out[-(y+1)][1] = num

    for y in range(N):
        num = ''
        for x in range(N-1, -1, -1):
            num += field[x][y]
        out[y][0] = num

    for a in range(N):
        print(*out[a])