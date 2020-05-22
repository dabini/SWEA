import heapq
T = int(input())
for t in range(T):
    V, E = map(int, input().split())
    adj = {i:[] for i in range(V+1)}
    for _ in range(E):
        s, e, w = map(int, input().split())
        adj[s].append([e, w])
        adj[e].append([s, w])

    INF = float('inf')
    key = [INF] * (V+1)
    mst = [0] * (V+1)
    result = 0
    pq = []

    key[0] = 0

    heapq.heappush(pq, (0,0))
    while pq:
        k, n = heapq.heappop(pq)
        if mst[n]:
            continue
        mst[n] = 1
        result += k

        for goal, cost in adj[n]:
            if not mst[goal] and key[goal] > cost:
                key[goal] = cost
                heapq.heappush(pq, (key[goal], goal))
    print("#{} {}".format(t+1, result))