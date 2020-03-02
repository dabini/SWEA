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



def DFS(x, y, k):
    stack.append(k)
    global cnt
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for d in range(4):
        newx = x + dx[d]
        newy = y + dy[d]
        if 0 <= newx < N and 0 <= newy < N and (newy,newx) not in visited:
            if room[newy][newx] == k+1:
                stack.append(k+1)

T = int(input())
for t in range(T):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]
    visited = []
    max_len = 0
    for j in range(N):
        for i in range(N):
            stack = []
            k = room[j][i]
            DFS(i, j, k)
            if max_len < len(stack):
                max_len = len(stack)
    print(max_len)