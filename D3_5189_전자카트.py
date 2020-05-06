from itertools import permutations

T = int(input())
for t in range(T):
    res = 987654321
    N = int(input())
    arr=[list(map(int, input().split())) for _ in range(N)]
    for p in permutations(range(1, N)):
        check= [0] + list(p) + [0]
        cnt=0
        for i in range(len(check) - 1):
            cnt+=arr[check[i]][check[i + 1]]
        if cnt<res:
            res=cnt
    print('#{} {}'.format(t+1, res))


# def DFS(start):
#     global sub_result, result, final_result
#
#     if len(sub_result) == N-1:
#         for i, j in sub_result:
#             result += Battery[i][j]
#
#         result += Battery[start][0]
#         final_result.append(result)
#         result = 0
#         return
#
#     for next in range(1, N):
#         if not visited[next]:
#             sub_result.append((start, next))
#             visited[next] = True
#             DFS(next)
#             sub_result.remove((start, next))
#             visited[next] = False
#
#
# TC = int(input())
# for tc in range(1, TC+1):
#     N = int(input())
#     Battery = [list(map(int, input().split())) for _ in range(N)]
#     visited = [0] * N
#     sub_result =  []
#     result = 0
#     final_result =[]
#     DFS(0)
#
#     print('#%d %d'%(tc, min(final_result)))