T = int(input())

for t in range(T):
    N = int(input())
    field = [[0 for _ in range(N)] for __ in range(N)]

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    x ,y = 0, 0
    field[y][x] = "1"
    k = 2
    d = 0

    while k <= N**2:
        if not(0 <= x+dx[d%4]<= N-1 and 0 <= y+dy[d%4] <= N-1) or field[y+dy[d%4]][x+dx[d%4]] != 0:
            d += 1
        y = y + dy[d % 4]
        x = x + dx[d % 4]
        field[y][x] = str(k)
        k += 1

    print("#{}".format(t+1))
    for i in range(N):
        print(" ".join(field[i]))

