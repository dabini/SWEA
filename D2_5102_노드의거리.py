def BFS(S):
    global res, k, G
    k += 1
    for x in range(V):
        if mymap[S][x] == 1 and not visited[x]:
            visited[x] = 1
            if x == G:
                res = k
                break
                return res
            else:
                BFS(x)
                k -= 1
        return

T = int(input())

for t in range(T):
    V, E = map(int, input().split()) #V노드의 개수, E 간선 정보
    mymap = [[0]*(V+1) for _ in range(V+1)]
    visited = [0]*(V+1)
    res = 0
    k = 0
    for e in range(E):
        start, end = map(int, input().split())
        mymap[start][end] = 1

    S, G = map(int, input().split())
    BFS(S)
    print(res)
