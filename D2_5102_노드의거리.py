def BFS(S):
    global check
    q.append(S)
    res.append(S)
    visited[S] = 1
    check = False
    while q:
        n = q.pop(0)
        for new in range(V+1):
            if mymap[n][new] and not visited[new]:
                visited[new] = visited[n] + 1
                q.append(new)
                res.append(new)
T = int(input())

for t in range(T):
    V, E = map(int, input().split()) #V노드의 개수, E 간선 정보
    mymap = [[0]*(V+1) for _ in range(V+1)]
    visited = [0]*(V+1)
    res = []
    q = []
    for e in range(E):
        start, end = map(int, input().split())
        mymap[start][end] = 1
        mymap[end][start] = 1

    S, G = map(int, input().split())
    BFS(S)
    # print(visited)
    print("#{}".format(t+1), end=" ")
    if visited[G] >0 :
        print(visited[G] -1)
    else:
        print(0)