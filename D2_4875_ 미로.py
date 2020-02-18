def getSome(x, y):
    global res, maze, visited
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    visited[y][x] = 1
    if maze[y][x] == 3:
        res = 1
        return
    for d in range(4):
        if 0<= x+dx[d] <N and 0<= y+dy[d] <N and maze[y+dy[d]][x+dx[d]] != 1 and not visited[y+dy[d]][x+dx[d]]:
            newx  = x+dx[d]
            newy = y+dy[d]
            getSome(newx, newy)

T = int(input())
for t in range(T):
    res = 0
    N = int(input())
    maze = [[0]*N for _ in range(N)]
    visited = [[0]*N for _ in range(N)]

    for m in range(N):
        maze[m] = list(map(int, input()))

    for y in range(N):
        for x in range(N):
            if maze[y][x] == 2:
                startx , starty = x, y
    getSome(startx, starty)
    print("#{} {}".format(t+1, res))




#스택
# dy = [-1, 0, 1, 0]
# dx = [0, 1, 0, -1]
# T = int(input())
# for case in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int,input())) for _ in range(N)]
#     TF = False
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] == 2:
#                 TF = True
#                 break
#         if TF:
#             break
#     result = 0
#     stack = [[i, j]]
#     visited = [[False] * N for _ in range(N)]
#     visited[i][j] = True
#     TF = False
#     while stack:
#         current = stack[-1]
#         y = current[0]
#         x = current[1]
#
#         for dir in range(4):
#             ny = y + dy[dir]
#             nx = x + dx[dir]
#
#             if 0 <= ny <= N-1 and 0 <= nx <= N-1:
#                 if arr[ny][nx] == 0 and not visited[ny][nx]:
#                     stack.append([ny, nx])
#                     visited[ny][nx] = True
#                     break
#
#                 elif arr[ny][nx] == 3:
#                     stack.append([ny, nx])
#                     TF = True
#                     result = 1
#                     break
#
#         else:
#             stack.pop()
#
#         if TF:
#             break
#     print(""#%d %d""%(case, result))"