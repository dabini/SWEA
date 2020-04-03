def f(n, k, s): #현재행, 전체행, n-1까지의 합
    global minV
    if n==k:
        if minV >s:
            minV = s
        return
    elif minV <= s: #합이 최소값보다 큰 경우(나머지 행을 굳이 따져볼 필요가 없으면 중지)
        return
    else:
        for i in range(k):
            if used[i] == 0:
                used[i] = 1
                f(n+1, k, s+A[n][i])
                used[i]= 0
        return
T = int(input())
for t in range(T):
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    used = [0]*N
    minV = 100
    f(0, N, 0)
    print("#{} {}".format(t+1, minV ))