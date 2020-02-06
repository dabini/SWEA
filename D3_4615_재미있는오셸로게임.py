T = int(input())

for t in range(T):
    N, M = map(int, input().split()) # 보드의 한 변의 길이 N과 플레이어가 돌을 놓는 횟수 M
    field = [[0]*N for _ in range(N)]

    for j in range(N//2-1, N//2+1): #기본 설정
        for i in range(N//2-1, N //2+1):
            if i == j: #색이 1이면 흑돌, 2이면 백돌
                field[j][i] = 2
            else:
                field[j][i] = 1

    dx = [1, -1, 0, 0, 1, -1, 1, -1] #대각선까지 포함
    dy = [0, 0, 1, -1, 1, -1, -1, 1]

    for m in range(M):
        X, Y, color = map(int, input().split())
        field[Y-1][X-1] = color

        for d in range(8):
            new = []
            check = True
            for k in range(2, N):
                if 0 <= Y-1+(dy[d]*k) < N and 0 <= X-1+(dx[d]*k) < N and field[Y-1+dy[d]*k][X-1+dx[d]*k]==color:
                        for f in range(1, k):
                            if field[Y-1+dy[d]*f][X-1+dx[d]*f] == 0:
                                check = False
                                break
                            if field[Y-1+dy[d]*f][X-1+dx[d]*f] != color and field[Y-1+dy[d]*f][X-1+dx[d]*f] != 0:
                                newx = X-1+dx[d]*f
                                newy = Y-1+dy[d]*f
                                new += [(newx, newy)]
                        if check:
                            for e in new:
                                x = e[0]
                                y = e[1]
                                field[y][x] = color
    Bcnt = 0
    Wcnt = 0
    for l in range(N):
        for q in range(N):
            if field[l][q] == 1:  #흑돌
                Bcnt += 1
            elif field[l][q] == 2: #백돌
                Wcnt += 1

    print("#{} {} {}".format(t+1, Bcnt, Wcnt))