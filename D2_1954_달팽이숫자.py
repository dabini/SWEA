<<<<<<< HEAD
def isSafe(lst, a, b):
    if lst[b][a] == 0:
        return True
    else:
        return False

=======
>>>>>>> 5a235df85c22ceeb064079074e84c027383f6903
T = int(input())

for t in range(T):
    N = int(input())
<<<<<<< HEAD
    k = 1
    snail = [[0 for _ in range(N)] for _ in range(N)]
    dir_y = [1, 0, -1, 0]
    dir_x = [0, 1, 0, -1]
    dir = 0
    x, y = 0, 0
    snail[y][x] = k

    while k < N**2:
        if x + dir_x[dir] >= 0 and dir_x[dir] < N and y + dir_y[dir] >= 0 and dir_y[dir] < N:
            if isSafe(snail, x + dir_x[dir], y + dir_y[dir]):
                k += 1
                x = x + dir_x[dir]
                y = y + dir_y[dir]
                snail[y][x] = k
            else:
                dir = (dir + 1) % 4
        else:
            dir = (dir + 1) % 4
    print(snail)


#
# def iz(x, y):
#     global L
#     if L[y][x] == 0:
#         return True
#     else:
#         return False
#
#
# T = int(input())
# for t in range(T):
#     n = int(input())
#     L = [[0] * n for _ in range(n)]
#
#     x = y = 0
#     dx = [1, 0, -1, 0]
#     dy = [0, 1, 0, -1]
#     dir = 0
#     i = 1
#     L[y][x] = i
#     while i < n ** 2:
#         if x + dx[dir] >= 0 and x + dx[dir] < n and y + dy[dir] >= 0 and y + dy[dir] < n:
#             if iz(x + dx[dir], y + dy[dir]):
#                 i += 1
#                 x = x + dx[dir]
#                 y = y + dy[dir]
#                 L[y][x] = i
#             else:
#                 dir = (dir + 1) % 4
#         else:
#             dir = (dir + 1) % 4
#     print('#{}'.format(t + 1))
#     for i in L:
#         print(*i)
=======
    field = [[0 for _ in range(N)] for __ in range(N)]

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    x ,y = 0, 0
    field[y][x] = "1"
    k = 2
    d = 0

    while k <= N**2:
        if not(0 <= x+dx[d%4]<= N-1 and 0 <= y+dy[d%4] <= N-1) or field[y+dy[d%4]][x+dx[d%4]] != 0:
            d += 1
        y = y + dy[d % 4]
        x = x + dx[d % 4]
        field[y][x] = str(k)
        k += 1

    print("#{}".format(t+1))
    for i in range(N):
        print(" ".join(field[i]))

>>>>>>> 5a235df85c22ceeb064079074e84c027383f6903
