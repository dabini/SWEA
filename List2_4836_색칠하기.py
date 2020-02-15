T = int(input())

for t in range(T):
    field = [[0] * 10 for _ in range(10)]
    N = int(input())
    for n in range(N):
        cnt = 0
        r1, c1, r2, c2, color = map(int, input().split())
        #r1, c1 =왼쪽위모서리인덱스 / r2, c2 = 오른쪽 아래 모서리 인덱스 #color (1빨강 2파랑)

        for y in range(c1, c2+1):
            for x in range(r1, r2+1):
                if field[y][x] == 0:
                   field[y][x] = color
                else:
                    field[y][x] = 3
        for j in range(10):
            for i in range(10):
                if field[j][i] == 3:
                    cnt += 1
    print("#{} {}".format(t+1, cnt))