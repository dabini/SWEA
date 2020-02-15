T = int(input())

for t in range(T):
    N, M = map(int, input().split()) # 보드의 한 변의 길이 N과 플레이어가 돌을 놓는 횟수 M
    field = [[0]*(N+2) for _ in range(N+2)]

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
        field[Y][X] = color

        for d in range(8):
            newx = X + dx[d]
            newy = Y + dy[d]
            if 0 <= newy < N and 0 <= newx < N and field[newy][newx]==color:
                cnt = 0
                while field[newy][newx] == color:

                # for f in range(1, k):
                #     if field[Y-1+dy[d]*f][X-1+dx[d]*f] == 0:
                #         check = False
                #         break
                #     if field[Y-1+dy[d]*f][X-1+dx[d]*f] != color and field[Y-1+dy[d]*f][X-1+dx[d]*f] != 0:
                #         newx = X-1+dx[d]*f
                #         newy = Y-1+dy[d]*f
                #         new += [(newx, newy)]
                # if check:
                #     for e in new:
                #         x = e[0]
                #         y = e[1]
                #             field[y][x] = color
    Bcnt = 0
    Wcnt = 0
    for l in range(N):
        for q in range(N):
            if field[l][q] == 1:  #흑돌
                Bcnt += 1
            elif field[l][q] == 2: #백돌
                Wcnt += 1

    print("#{} {} {}".format(t+1, Bcnt, Wcnt))



#from pprint import pprint
#
# T=int(input())
# for z in range(T):
#     n,m = list(map(int,input().split()))
#     map_list = [[99 for _ in range(n+2)] for _ in range(n+2)] #판 만들기  n+2 * n+2 벽을 만들기
#
#     #기본 세팅:
#     map_list[n//2][n//2]=1
#     map_list[n//2+1][n//2]=0
#     map_list[n//2+1][n//2+1]=1
#     map_list[n//2][n//2+1]=0
#
#
#     dy=[0,0,1,-1,1,-1,-1,1]
#     dx=[1,-1,0,0,1,1,-1,-1]
#     #배치 위치는 [x][y] 가 된다. 돌은 dol-1을 넣는다.
#     for i in range(m):
#         x,y,dol = list(map(int,input().split()))
#         a=dol-1  #검은돌 0, 흰색돌1
#         map_list[x][y]=a
#         for j in range(8):
#             newX=x+dx[j]
#             newY=y+dy[j]
#             if map_list[newX][newY]==1-a:
#                 cnt=0
#                 while map_list[newX][newY]==1-a:
#                     newX+=dx[j]
#                     newY+=dy[j]
#                     cnt+=1
#                     if map_list[newX][newY]==99:
#                         cnt=0
#                         break
#                     ##즉 a돌을 만나면 cnt그대로 있고 아니면 cnt =0
#                 newX = x + dx[j]
#                 newY = y + dy[j]
#                 if cnt!=0:
#                     for _ in range(cnt):
#                         map_list[newX][newY]=a
#                         newX += dx[j]
#                         newY += dy[j]
#         # print("{} {} {}".format(i+1,x,y))
#         # pprint(map_list)
#         # print()
#     #counting하고 출력하기
#     cnt_b=0
#     cnt_w=0
#     for i in range(1,n+1):
#         for j in range(1,n+1):
#            if map_list[i][j]==0:
#                 cnt_b+=1
#            elif map_list[i][j]==1:
#                 cnt_w+=1
#     print("#{} {} {}".format(z+1,cnt_b,cnt_w))