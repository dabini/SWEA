def f(n, k, s): #순열의 n 번 원소 결정
    global maxV
    if s <= maxV: #모든 일에 대해 사람이 정해지면, 이전의 최대 성공확률과 비교
        return
    if n == k:
        if maxV < s:
            maxV = s
        return

    else:
        for i in range(k):
            if used[i] == 0:
                used[i] = 1
                f(n+1, k, s*board[i][n]/100)
                used[i] = 0

T = int(input())
for t in range(T):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    used = [0] * N
    p = [0] * N
    maxV = 0
    f(0, N, 1)
    print("#%d %.6f"%(t+1, maxV*100))