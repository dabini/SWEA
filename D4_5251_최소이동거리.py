T = int(input())
for t in range(T):
    N, E = map(int, input().split())
    adj = {i : [] for i in range(N+1)}
    for _ in range(E):
        s, e, w = map(int, input().split())
        adj[s].append([e, w])

    INF = float('inf')
    d = [INF] * (N+1)
    selected = [0] * (N+1)

    d[0] = 0
    cnt = 0

    while cnt < N:
        min = INF
        u = -1
        for i in range(N+1):
            if not selected[i] and d[i] < min:
                min = d[i]
                u = i

        selected[u] = 1
        cnt += 1

        for g, cost in adj[u]:
            if d[g] > d[u] + cost:
                d[g] = d[u] + cost
    print("#{} {}".format(t+1, d[N]))