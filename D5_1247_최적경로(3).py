def getD(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def perm(n, k, cur_dist):
    global ans
    if cur_dist > ans:
        return
    if k == n:
        cur_dist += D[t[k]][t[N+1]]
        if cur_dist < ans:
            ans = cur_dist
    else:
        for i in range(n):
            if visited[i+1]:
                continue
            t[k+1] = i+1
            visited[i+1] = 1
            perm(n, k+1, cur_dist+D[t[k]][t[k+1]])
            visited[i+1] = 0

T = int(input())
for tc in range(T):
    N = int(input())
    temp = list(map(int, input().split()))
    t = [0] + [0] * N + [N+1]
    visited = [0] * (N+2)
    P = [(0, 0) for _ in range(N+2)]
    D = [[0 for _ in range(N+2)] for _ in range(N+2)]
    ans = 0x7fffffff

    P[0] = (temp[0], temp[1])
    P[N+1] = (temp[2], temp[3])

    idx = 1

    for i in range(4, len(temp), 2):
        P[idx] = (temp[i], temp[i+1])
        idx += 1

    for i in range(N+1):
        for j in range(i+1, N+2, 1):
            D[j][i] = D[i][j] = getD(P[i], P[j])

    perm(N, 0, 0)
    print("#{} {}".format(tc+1, ans))