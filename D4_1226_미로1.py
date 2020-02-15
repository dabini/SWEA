import sys
sys.stdin = open("input1.txt", 'r')

# def Getsome(y, x):
#     global res
#     if not 0<=x< 16 or not 0<=y<16 or field[y][x] ==1 or res == 1:  #res == 1이 없으면 3을 찾아도 끝까지 찾아봄!
#         return
#     if field[y][x] == 3:
#         res = 1
#         return
#
#     field[y][x] = 1
#     Getsome(y+1, x)
#     Getsome(y-1, x)
#     Getsome(y, x+1)
#     Getsome(y, x-1)
#
# for _ in range(10):
#     t = int(input())
#     field = [[0]*16 for _ in range(16)]
#     res = 0
#
#     for k in range(16):
#         field[k] = list(map(int, input()))
#
#
#     for y in range(16):
#         for x in range(16):
#             if field[y][x] == 2:
#                 newy = y
#                 newx = x
#     # print(field)
#
#     Getsome(newx, newy)
#     print("#{} {}".format(t, res))

def DFS(x, y):
    global field, res
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    field[y][x] = 1

    for d in range(4):
        if not 0 <= x+dx[d] < 16 or not 0 <= y+dy[d] < 16 or field[y+dy[d]][x+dx[d]] == 1 or res == 1:
            return
        if field[y+dy[d]][x+dx[d]] == 3:
            res = 1
            return

for _ in range(10):
    t = int(input())
    field = [[0]*16 for _ in range(16)]
    res = 0

    for k in range(16):
        field[k] = list(map(int, input()))

    for y in range(16):
        for x in range(16):
            if field[y][x] == 2:
                newy = y
                newx = x
    # print(field)

    DFS(newx, newy)
    print("#{} {}".format(t, res))