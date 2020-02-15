def Stack(S):
    global field, G, ans
    visited[S] = 1

    for v in range(1, V+1):
        if field[S][v] == 1 and not visited[v]:
            if v == G:
                ans = 1
                return
            Stack(v)

T = int(input())

for t in range(T):
    V, E = map(int, input().split())
    field = [[0]*(V+1) for _ in range(V+1)]
    visited = [0]*(V+1)
    ans = 0

    for e in range(E):
        start, end = map(int, input().split())
        field[start][end] = 1
        # indeg[end] += 1
        # outdeg[start] += 1


    S, G = map(int, input().split())
    Stack(S)
    print("#{} {}".format(t+1, ans))