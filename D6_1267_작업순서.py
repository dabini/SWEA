# def DFS(indeg):
#     global field, V, out
#     for f in range(len(indeg)):
#         if indeg[f] == 0:
#             out.append(f+1)
#             for now in range(V):
#                 if field[f][now] and indeg[now]:
#                     field[f][now] -=1
#                     indeg[now] -= 1
#                     DFS(now)
#
# for t in range(10):
#     V, E = map(int, input().split()) #V 그래프의 정점의 총 수 E 간선의 총 수
#     V_lst = list(map(int, input().split()))
#
#     field = [[0] * V for _ in range(V)]
#     out = []
#     indeg = [0] * V
#
#     for i in range(E):
#         start = V_lst[2*i]
#         end = V_lst[2*i+1]
#         field[start-1][end-1] += 1
#         indeg[end-1] += 1
#
#     DFS(indeg)
#     out = list(map(str, out))
#     print("#{} {}".format(t+1, " ".join(out)))


#
# def DFS(here):
#     global field, V, indeg, out
#     out.append(here+1)
#     indeg[here] = -1
#     for now in range(V):
#         if now+1 not in out:
#             if field[here][now] and indeg[now]:
#                 field[here][now] -=1
#                 DFS(now)
#             elif indeg[now] == 0:
#                 DFS(now)
#
# for t in range(1):
#     V, E = map(int, input().split()) #V 그래프의 정점의 총 수 E 간선의 총 수
#     V_lst = list(map(int, input().split()))
#     # visited = [0] * V
#     field = [[0] * V for _ in range(V)]
#     out = []
#     indeg = [0] * V
#
#     for i in range(E):
#         start = V_lst[2*i]
#         end = V_lst[2*i+1]
#         field[start-1][end-1] = 1
#         indeg[end-1] += 1
#
#     here = indeg.index(0)
#     DFS(here)
#     out = list(map(str, out))
#     print("#{} {}".format(t+1, " ".join(out)))



def DFS(indeg):
    global field, V, out
    for here in range(V):
        if indeg[here] == 0 and (here+1) not in out:
            out.append(here+1)
        for now in range(V):
            if field[here][now] == 1:
                field[here][now] = 0
                indeg[now] -= 1
        DFS(indeg)


for t in range(1):
    V, E = map(int, input().split()) #V 그래프의 정점의 총 수 E 간선의 총 수
    V_lst = list(map(int, input().split()))
    field = [[0] * V for _ in range(V)]
    out = []
    indeg = [0] * V

    for i in range(E):
        start = V_lst[2*i]
        end = V_lst[2*i+1]
        field[start-1][end-1] = 1
        indeg[end-1] += 1


    DFS(indeg)
    out = list(map(str, out))
    print("#{} {}".format(t+1, " ".join(out)))