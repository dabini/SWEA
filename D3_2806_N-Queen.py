def nqueen(n):
    global cnt
    if n == N:
        cnt += 1
        return
    for y in range(N):
        if row[y] + left[y+n] + right[N-1+n-y] == 0:
            row[y] = left[y + n] = right[N - 1 + n - y] = 1
            nqueen(n+1)
            row[y] = left[y + n] = right[N - 1 + n - y] = 0


T = int(input())
for t in range(T):
    N = int(input())
    cnt = 0
    row = [0 for _ in range(N)]
    left = [0 for _ in range(2*N-1)]
    right = [0 for _ in range(2*N-1)]

    nqueen(0)
    print("#{} {}".format(t+1, cnt))