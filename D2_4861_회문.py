T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    field = [[0]*N for _ in range(N)]
    res = ''

    for n in range(N):
        field[n] = list(map(str, input()))


    for y in range(N-(N-M)):
        for x in range(N-(N-M)):
            for ym in range(y, y+M):
                lst = ''
                for xm in range(x, x+M):
                    lst += field[ym][xm]
                if lst == lst[::-1]:
                    res = lst
        break

    for y in range(N-(N-M)):
        for x in range(N-(N-M)):
            for ym in range(y, y+M):
                lst = ''
                for xm in range(x, x+M):
                    lst += field[xm][ym]
                if lst == lst[::-1]:
                    res = lst
                    break

    print(res)