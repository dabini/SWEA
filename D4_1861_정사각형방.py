# import sys
# sys.setrecursionlimit(10**8)
# def DFS(x, y, k):
#     global cnt
#     dx = [1, -1, 0, 0]
#     dy = [0, 0, 1, -1]
#     for d in range(4):
#         newx = x + dx[d]
#         newy = y + dy[d]
#         if 0 <= newx < N and 0 <= newy < N:
#             if room[newy][newx] == k+1:
#                 cnt += 1
#                 DFS(newx, newy, k+1)
#
# T = int(input())
# for t in range(T):
#     N = int(input())
#     room = [list(map(int, input().split())) for _ in range(N)]
#     cnt_lst = [[0]*N for _ in range(N)]
#     for j in range(N):
#         for i in range(N):
#             cnt = 1
#             k = room[j][i]
#             DFS(i, j, k)
#             cnt_lst[j][i] = cnt
#     # print(cnt_lst)
#     max_num = 0
#     check = []
#     for y in range(N):
#         for x in range(N):
#             if cnt_lst[y][x] > max_num:
#                 max_num = cnt_lst[y][x]
#
#     for a in range(N):
#         for b in range(N):
#             if cnt_lst[a][b] == max_num:
#                 check.append((a, b))
#     res = []
#     for c in check:
#         res.append(room[c[0]][c[1]])
#
#     print("#{} {} {}".format(t+1, min(res),max_num))


#길이 줄여서 다시
# def DFS(r, c):
#     global length
#     for d in range(4):
#         x1 = r + dx[d]
#         y1 = c + dy[d]
#         if 0 <= x1 < N and 0 <= y1 < N:
#             if board[x1][y1] == board[r][c] + 1:
#                 if visit[x1][y1] == 0:
#                     DFS(x1, y1)
#                 else:
#                     visit[r][c] = visit[x1][y1] + 1
#                     return
#     length += 1
#     visit[r][c] = length
#
#
# T = int(input())
# for t in range(T):
#     N = int(input())
#     board = [list(map(int, input().split())) for _ in range(N)]
#     visit = [[0] * N for _ in range(N)]
#     dx = [0, 0, -1, 1]
#     dy = [-1, 1, 0, 0]
#     for i in range(N):
#         for j in range(N):
#             if visit[i][j] == 0:
#                 length = 0
#                 DFS(i, j)
#     result = 0
#     room_number = 876543221
#     for u in range(N):
#         result = max(result, max(visit[u]))
#     for k in range(N):
#         for y in range(N):
#             if visit[k][y] == result:
#                 room_number = min(room_number, board[k][y])
#     print('#{} {} {}'.format(t+1, room_number, result))
#
#


#교수님 코드

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    rm = [list(map(int, input().split())) for _ in range(N)]
    v = [0]*(N*N+1)

    for i in range(N):
        for j in range(N):
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]

                if 0 <= ni < N and 0 <= nj < N and rm[i][j]+1 == rm[ni][nj]:
                    v[rm[i][j]] =1 #1차이나는 방 표시

    cnt = 0
    maxV = 0
    st = 0  #최대 구간 인덱스

    for i in range(N*N, -1, -1): #v[0]까지 확인
        if v[i] == 1:           #이웃간의 i+1이 있는 경우
            cnt += 1            #연속한 1의 개수
        else:                   #0을 만나면
            if maxV<=cnt:       #길이가 같으면 왼쪽 구간 선택
                maxV = cnt      #구간의 최대 길이
                st = i +1       #가장 긴 구간의 시작 인덱스
            cnt = 0
    print("#{} {} {}".format(tc, st, maxV+1))
