T = int(input())
for t in range(T):
    N, S = map(str, input().split())
    N = int(N)
    game = [[0]*N for _ in range(N)]
    res = [[0]*N for _ in range(N)]
    ans = [[0]*N for _ in range(N)]
    for n in range(N):
        game[n] = list(map(int, input().split()))

    if S == 'up':
        for y in range(N):
            lst = []
            for x in range(N):
                if game[x][y] != 0:
                    lst += [game[x][y]]
            out = []
            k = 1
            while True:
                if len(lst) ==  1:
                    out += [lst[0]]
                    break
                elif len(lst) <1:
                    break
                temp = lst[0]
                if temp == lst[k]:
                    out += [2*temp]
                    lst.pop(k)
                    lst.pop(k-1)
                else:
                    out += [temp]
                    lst.pop(k-1)

            out += [0] * (N - len(out))
            res[y] = out

        for j in range(N):
            for i in range(N):
                ans[j][i] = res[i][j]

    elif S == 'down':
        for y in range(N):
            lst = []
            for x in range(N):
                if game[x][y] != 0:
                    lst += [game[x][y]]
            lst = lst[::-1]
            out = []
            k = 1
            while True:
                if len(lst) == 1:
                    out += [lst[0]]
                    break
                elif len(lst) < 1:
                    break
                temp = lst[0]
                if temp == lst[k]:
                    out += [2 * temp]
                    lst.pop(k)
                    lst.pop(k - 1)
                else:
                    out += [temp]
                    lst.pop(k - 1)

            out += [0] * (N - len(out))
            res[y] = out

        for j in range(N):
            for i in range(N):
                ans[-(j+1)][i] = res[i][j]

    elif S == 'left':
        for y in range(N):
            lst = []
            for x in range(N):
                if game[y][x] != 0:
                    lst += [game[y][x]]

            out = []
            k = 1
            while True:
                if len(lst) == 1:
                    out += [lst[0]]
                    break
                elif len(lst) < 1:
                    break
                temp = lst[0]
                if temp == lst[k]:
                    out += [2 * temp]
                    lst.pop(k)
                    lst.pop(k - 1)
                else:
                    out += [temp]
                    lst.pop(k - 1)

            out += [0] * (N - len(out))
            res[y] = out
        ans = res


    elif S == 'right':
        for y in range(N):
            lst = []
            for x in range(N):
                if game[y][x] != 0:
                    lst += [game[y][x]]

            lst = lst[::-1]
            out = []
            k = 1
            while True:
                if len(lst) == 1:
                    out += [lst[0]]
                    break
                elif len(lst) < 1:
                    break
                temp = lst[0]
                if temp == lst[k]:
                    out += [2 * temp]
                    lst.pop(k)
                    lst.pop(k - 1)
                else:
                    out += [temp]
                    lst.pop(k - 1)

            out += [0] * (N - len(out))
            res[y] = out

        for j in range(N):
            ans[j] = res[j][::-1]


    print("#{}".format(t+1))
    for n in range(N):
        print(*ans[n])