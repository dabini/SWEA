T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    field = [[0]*N for _ in range(N)]

    for i in range(N):
        field[i] = list(map(int, input().split()))

    lst = []
    for y in range(N-M+1):
        for x in range(N-M+1):
            cnt = 0
            for z in range(M):
                for v in range(M):
                    cnt += field[y+z][x+v]
            lst += [cnt]
    max_num = max(lst)

    print("#{} {}".format(t+1, max_num))