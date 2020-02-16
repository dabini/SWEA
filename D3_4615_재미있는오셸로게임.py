T = int(input())

for t in range(T):
    N, M = map(int, input().split()) # 보드의 한 변의 길이 N과 플레이어가 돌을 놓는 횟수 M
    field = [[0]*(N+1) for _ in range(N+1)]

    for j in range(N//2, N//2+2): #기본 설정
        for i in range(N//2, N//2+2):
            if i == j: #색이 1이면 흑돌, 2이면 백돌
                field[j][i] = 2
            else:
                field[j][i] = 1

    dx = [1, -1, 0, 0, 1, -1, 1, -1] #대각선까지 포함
    dy = [0, 0, 1, -1, 1, -1, -1, 1]

    for m in range(M):
        X, Y, color = map(int, input().split())
        field[Y][X] = color

        for d in range(8):
            check = True
            for k in range(1, N):
                if 1 <= Y+(dy[d]*k) < N+1 and 1<=X+(dx[d]*k)< N+1 and field[Y+(dy[d]*k)][X+(dx[d]*k)] == color:
                    for f in range(1, k):
                        if field[Y+dy[d]*f][X+dx[d]*f] == 0:
                            check = False
                            break
                    if check == False:
                        break
                    if check:
                        for f in range(1, k):
                            field[Y+dy[d]*f][X+dx[d]*f] = color
                        break

    Bcnt = 0
    Wcnt = 0
    for l in range(1, N+1):
        for q in range(1, N+1):
            if field[l][q] == 1:  #흑돌
                Bcnt += 1
            elif field[l][q] == 2: #백돌
                Wcnt += 1

    print("#{} {} {}".format(t+1, Bcnt, Wcnt))