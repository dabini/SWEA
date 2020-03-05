def find(x, y, tmp):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    tmp += str(board[y][x])
    if len(tmp) == 7:
        res.add(tmp)
        return
    else:
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            if 0 <= ny < 4 and 0 <= nx < 4:
                find(nx, ny, tmp)

T = int(input())
for t in range(T):
    res = set()
    board = [list(map(int, input().split())) for _ in range(4)]
    # print(board)
    for j in range(4):
        for i in range(4):
            tmp = ''
            find(j, i, tmp)

    print("#{} {}".format(t+1, len(res)))