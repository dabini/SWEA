T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    arr = [list(map(str, input())) for _ in range(N)]

    min_num = 987654321
    for i in range(0, N-3+1):
        for j in range(i+1, N-2+1):
            cnt = 0
            for y in range(0, i+1):
                for x in range(M):
                    if arr[y][x] != "W":
                        cnt += 1
            for b in range(i+1, j+1):
                for a in range(M):
                    if arr[b][a] != "B":
                        cnt += 1
            for d in range(j+1, N):
                for c in range(M):
                    if arr[d][c] != "R":
                        cnt += 1
            if min_num > cnt:
                min_num = cnt
    print("#{} {}".format(t+1, min_num))