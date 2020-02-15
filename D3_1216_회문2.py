for _ in range(10):
    t = int(input())
    field = [[0]*100 for _ in range(100)]
    res = 0
    for i in range(100):
        field[i] = list(map(str, input()))

    for y in range(100):
        checkx = []
        checky = []
        for x in range(100):
            checkx += field[y][x]
            checky += field[x][y]

    #
    #     start = 0
    #     end = 99
    #     ans = 2
    #     while start <= 50 and end >= 50:
    #         if checkx[start] == checkx[end]:
    #             if start == end:
    #                 ans += 1
    #             else:
    #                 ans += 2
    #             start += 1
    #             end -= 1
    #         else:
    #             ans = 2
    #             start += 1
    #             end -= 1
    #         if ans > res:
    #             res = ans
    #
    #     while start <= 50 and end >= 50:
    #         if checky[start] == checky[end]:
    #             if start == end:
    #                 ans += 1
    #             else:
    #                 ans += 2
    #             start += 1
    #             end -= 1
    #         else:
    #             ans = 2
    #             start += 1
    #             end -= 1
    #
    #         if ans > res:
    #             res = ans
    # print(res)