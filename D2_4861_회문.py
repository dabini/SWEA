T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    field = [[0]*N for _ in range(N)]
    res = ''

    for n in range(N):
        field[n] = list(map(str, input()))

    for y in range(N):
        lst = []
        lst2 = []
        for x in range(N):
            lst += field[y][x]
            lst2 += field[x][y]

        for j in range(N-M+1):
            check = []
            for i in range(j, j+M):
                check += lst[i]
            if check == check[::-1]:
                res = check

        for j in range(N-M+1):
            check2 = []
            for i in range(j, j+M):
                check2 += lst2[i]
            if check2 == check2[::-1]:
                res = check2

    print("#{} {}".format(t+1,''.join(res)))