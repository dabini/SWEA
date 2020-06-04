dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    q = []
    q.append((x, y))
    visited[y][x] = 1
    dist[0][0] = arr[0][0]
    while q:
        i, j = q.pop(0)
        for d in range(4):
            ni, nj = i + dx[d], j+dy[d]
            if 0 <= ni < N and 0 <= nj < N:
                if not visited[nj][ni] or dist[j][i] + arr[nj][ni] < dist[nj][ni]:
                    dist[nj][ni] = dist[j][i] + arr[nj][ni]
                    q.append((ni, nj))
                    visited[nj][ni] = 1


T = int(input())
for t in range(T):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    dist = [[987654321 for _ in range(N)] for _ in range(N)]
    bfs(0, 0)
    print("#{} {}".format(t+1, dist[N-1][N-1]))