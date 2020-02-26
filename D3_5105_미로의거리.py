def bfs(y, x):
    visited[y][x] += 1
    queue.append((y, x))
    global N, res
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    while queue:
        y, x = queue.pop(0)
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            if 0<= ny < N and  0<= nx < N:
                if maze[ny][nx] != 1 and not visited[ny][nx]:
                    queue.append((ny, nx))
                    visited[ny][nx] += 1
                    distance[ny][nx] = distance[y][x] + 1
                    if maze[ny][nx] == 3:
                        res = distance[ny][nx] -1
                        return


T = int(input())
for t in range(T):
    res = 0
    N = int(input())
    maze = [list(map(int,input())) for _ in range(N)]
    queue = []
    visited = [[0]*N for _ in range(N)]
    distance = [[0] * N for _ in range(N)]


    for j in range(N):
        for i in range(N):
            if maze[j][i] == 2:
                starty, startx = j, i
    bfs(starty, startx)
    print("#{} {}".format(t+1, res))