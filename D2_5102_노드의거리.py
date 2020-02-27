def BFS(S, G):
    global res
    q.append(S)
    while q:
        n = q.pop(0)
        if n not in visited:
            visited.append(n)
            q

T = int(input())

for t in range(T):
    V, E = map(int, input().split()) #V노드의 개수, E 간선 정보
    mymap = [[0]*(V+1) for _ in range(V+1)]
    visited = [0]*(V+1)
    res = 0
    k = 0
    q = []
    for e in range(E):
        start, end = map(int, input().split())
        mymap[start][end] = 1

    S, G = map(int, input().split())
    BFS(S)
    print(res)
