def Find(y, x):
    global res, M, k, num
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    k = k+1
    for d in range(4):
        ny = y + dy[d]
        nx = x + dx[d]
        if 0<= ny<M and 0 <= nx< M and field[ny][nx] == check_lst[k] and not visited[ny][nx]:
            visited[ny][nx] = 1
            if k < (num-1):
                Find(ny, nx)
            elif k == (num-1):
                res = 1
                break
    return res

T = int(input())
for t in range(T):
    lst = list(map(int, input().split()))
    num = lst[0]
    check_lst = lst[1:]
    M = int(input())
    field = [list(map(int, input().split())) for _ in range(M)]
    visited = [[0]*M for _ in range(M)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    res = 0
    k = 0
    for y in range(M):
        for x in range(M):
            if field[y][x] == check_lst[k]:
                newy, newx = y, x
                break
    Find(newy,newx)
    print("#{} {}".format(t+1, res))