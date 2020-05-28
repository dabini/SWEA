T = int(input())
for t in range(T):
    cust_num = int(input())
    loc = list(map(int, input().split()))
















# for T in range(1, int(input()) + 1):
#     N = int(input())
#     data = list(map(int, input().split()))
#     visited = [0] * (N + 2)
#     visited[0] = visited[1] = 1
#     nodes = []
#     mini = 99999999999
#     for i in range(0, N * 2 + 4, 2):
#         nodes.append([data[i], data[i + 1]])
#
#
#     def dfs(node, depth, tot):
#         global mini
#         if depth == N:
#             t = tot + abs(node[0] - nodes[1][0]) + abs(node[1] - nodes[1][1])
#             if t < mini:
#                 mini = t
#                 return
#         for i in range(N + 2):
#             if not visited[i]:
#                 t = tot + abs(node[0] - nodes[i][0]) + abs(node[1] - nodes[i][1])
#                 if t > mini:
#                     continue
#                 visited[i] = 1
#                 dfs(nodes[i], depth + 1, t)
#                 visited[i] = 0
#
#
#     dfs(nodes[0], 0, 0)
#     print('#{} {}'.format(T, mini))