T = int(input())

for t in range(T):
    N = int(input())
    maze = [[0]*N for _ in range(N)]

    for m in range(N):
        maze[m] = list(map(int, input()))
