def DFS(y, tmp):
    global res

    if y == N:
        if res > tmp:
            res = tmp
        return

    if res < tmp:
        return

    for x in range(N):
        if not visited[x]:
            visited[x] = True
            DFS(y + 1, tmp + arr[y][x])
            visited[x] = False

T = int(input())
for t in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0]*N
    res = 987654321
    DFS(0, 0)
    print("#{} {}".format(t+1, res))