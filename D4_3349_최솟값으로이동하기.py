# T = int(input())
# for t in range(T):
#     Y, X, N = map(int, input().split())
#     res = 0
#     for n in range(N):
#         x, y = map(int, input().split())
#         while x-1 and y-1:
#             x -= 1
#             y -= 1
#             res += 1
#         while x-1 or y-1:
#             if x-1:
#                 x -= 1
#                 res += 1
#             elif y-1:
#                 y -=1
#                 res +=1
#
#     print("#{} {}".format(t+1, res))

T = int(input())
for t in range(T):
    W, H, N = map(int, input().split())
    lst = [0] * N
    for n in range(N):
        lst[n] = list(map(int, input().split()))
    startX, startY = map(int, lst[0])
    result = 0
    for n in range(1, N):
        endX, endY = map(int, lst[n])
        if endX >= startX and endY >= startY:
            X = endX - startX
            Y = endY - startY
            if X > Y:
                result += X
            else:
                result += Y

        elif endX > startX and endY < startY:
            X = endX - startX
            Y = startY - endY
            result += (X + Y)
        elif endX < startX and endY > startY:
            X = startX - endX
            Y = endY - startY
            result += (X + Y)
        startX, startY = endX, endY
    print('#{} {}'.format(t+1, result))