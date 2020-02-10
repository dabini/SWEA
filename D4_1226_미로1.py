import sys
sys.stdin = open("input1.txt", 'r')

def DFS(x, y):
    global field, res, visited, xcheck, ycheck
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    visited[y][x] = 1
    ycheck += [y]
    xcheck += [x]
    for d in range(4):
        if 0 <= x+dx[d] < 16 and 0 <= y+dy[d] < 16 and field[y+dy[d]][x+dx[d]] == 3:
            res = 1
            return
        elif 0<= x+dx[d] < 16 and 0 <= y+dy[d]< 16 and field[y+dy[d]][x+dx[d]] == 0 and not visited[y+dy[d]][x+dx[d]]:
            return DFS(x + dx[d], y + dy[d])
        # elif 0 <= x + dx[d] < 16 and 0 <= y + dy[d] < 16 and field[y + dy[d]][x + dx[d]] == 0 and visited[y + dy[d]][x + dx[d]]:
        elif 0<= x+dx[d] < 16 and 0 <= y+dy[d]< 16 and field[y+dy[d]][x+dx[d]] == 0 and not visited[y+dy[d]][x+dx[d]]:
            while True:
                if 0 <= ycheck[-1]+dy[d]<16 and 0 <=xcheck[-1]+dx[d]<16 and not visited[ycheck[-1]+dy[d]][xcheck[-1]+dx[d]]:
                    return DFS(xcheck[-1]+dx[d], ycheck[-1]+dy[d])
                    break
                else:
                    ycheck.pop()
                    xcheck.pop()

for _ in range(10):
    t = int(input())
    field = [[0]*16 for _ in range(16)]
    res = 0
    ycheck = []
    xcheck = []
    for k in range(16):
        field[k] = list(map(int, input()))

    visited = [[0]*16 for _ in range(16)]
    for y in range(16):
        for x in range(16):
            if field[y][x] == 2:
                newy = y
                newx = x
    # print(field)

    DFS(newx, newy)
    print(res)