T = int(input())

for t in range(T):
    N, K = map(int, input().split())

    puzzle = [0]*N
    puzzle2 = [[0]*N for _ in range(N)]

    for i in range(N):
        puzzle[i] = list(map(int, input().split()))

    for y in range(N):
        for x in range(N):
            puzzle2[y][x] = puzzle[x][y]

    cnt = 0
    for y in range(N):
        for x in range(N-K+1):
            xx = x
            while xx < N and puzzle[y][xx] ==1:
                puzzle[y][xx] = 0
                xx +=1
            if xx-x == K:
                cnt += 1

        for y in range(N):
            for x in range(N - K + 1):
                xx = x
                while xx < N and puzzle2[y][xx] == 1:
                    puzzle2[y][xx] = 0
                    xx += 1
                if xx - x == K:
                    cnt += 1

    print("#{} {}".format(t+1, cnt))