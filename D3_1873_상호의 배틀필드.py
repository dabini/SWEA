T = int(input())
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
order_dict = {"U":0, "D":1, "L": 2,"R":3 ,"S":4 }
tank = '^v<>'
for t in range(T):
    H, W = map(int, input().split())
    field = [list(input()) for _ in range(H)]
    order_num = int(input())
    orders = list(input())
    for h in range(H):
        for w in range(W):
            if field[h][w] in tank:
                x, y = w, h
                d = tank.index(field[h][w])

    for order in orders:
        if order_dict[order] == 4: #사격
            #현재 위치는 x,y 방향 = d
            tx, ty = x+ dx[d], y+dy[d]
            while 0 <= tx < W and 0 <= ty <H:
                if field[ty][tx] == "#":
                    break
                if field[ty][tx] == "*":
                    field[ty][tx] = "."
                    break
        else:
            #방향을 전환하고 그방향으로 전진
            #만약 벽이나 물이면 안돼
            d = order_dict[order]
            field[y][x] = tank[d]
            tx, ty = x + dx[d], y + dy[d]
            if 0 <= tx < W and 0 <= ty <H and field[ty][tx] == ".":
                field[ty][tx] = "."
                x, y = tx, ty
                field[y][x] = tank[d]
    print("#{}".format(t+1), end=" ")
    [print(''.join(x)) for x in field]

# cmd={'U':0,'D':1,'L':2,'R':3,'S':4}
# tank='^v<>'
# dx=[-1,1,0,0]
# dy=[0,0,-1,1]
# for t in range(int(input())):
#     H,W=map(int,input().split())
#     arr=[list(input()) for _ in range(H)]
#     textl=int(input())
#     text=input()
# # 전차의 위치와 상태
#     si,sj=-1,-1
#     for i in range(H):
#         for j in range(W):
#             if arr[i][j] in tank:
#                 di=tank.index(arr[i][j])
#                 si=i
#                 sj=j
#                 break
#         if si!=-1:
#             break
#     for ch in text:
#         r=1
#         if cmd[ch]==4:
#             while True:
#                 ni=si+r*dx[di]
#                 nj=sj+r*dy[di]
#                 if 0<=ni<H and 0<=nj<W:
#                     if arr[ni][nj]=='*':
#                         arr[ni][nj]='.'
#                         break
#                     elif arr[ni][nj]=='#':
#                         break
#                 else:
#                     break
#                 r+=1
#         else:
#             di=cmd[ch]
#             ni=si+dx[di]
#             nj=sj+dy[di]
#             if 0<=ni<H and 0<=nj<W and arr[ni][nj]=='.':
#                 arr[si][sj]='.'
#                 si=ni
#                 sj=nj
#             arr[si][sj]=tank[di]
#     print('#{}'.format(t+1), end=' ')
#     [print(''.join(row)) for row in arr]