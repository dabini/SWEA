import itertools
# def bolt(n, lst):
#     for i in range()
T = int(input())
for t in range(T):
    n = int(input())
    lst = list(map(int, input().split()))

    # print(list(map(list, itertools.permutations(lst))))
    data = list(map(list, itertools.permutations(lst)))
    # print(data)
    for i in range(1, 2*n - 2, 2):
        for k in data:
            if k[i] == k[i+1]:
                k = k[:]
                break
    print(k)

# T = int(input())
#
# for t in range(T):
#     lst = []
#
#     lst_num = int(input())
#     lst_data = list(map(int, input().split()))
#
#     for i in range(0, len(lst_data), 2):
#         lst.append([lst_data[i], lst_data[i + 1]])
#
#     max_list = []
#
#     def Bolt(idx, used, ans):
#         global max_list
#
#         ans.append(lst[idx][0])
#         ans.append(lst[idx][1])
#         used[idx] = True
#         flag = 0
#
#         for i in range(len(lst)):
#             if used[i]:
#                 continue
#
#             if lst[i][0] == lst[idx][1]:
#                 Bolt(i, used, ans)
#                 flag = 1
#
#         if flag == 0:
#             # print('m:',max_list)
#             # print('a:',ans)
#             if len(max_list) < len(ans):
#                 max_list.clear()
#                 for i in ans:
#                     max_list.append(i)
#             # print('m1:', max_list)
#             # print('a1:', ans)
#         # print(ans)
#         ans.pop()
#         ans.pop()
#         used[idx] = False
#         # return ans_tmp
#
#
#     for i in range(len(lst)):
#         ans = []
#         used = [False for _ in range(len(lst))]
#         Bolt(i, used, ans)
#
#     print('#%d' % (t + 1), end=' ')
#     print(*max_list)


#다른 코드
# T = int(input())
#
# for i in range(T):
#     N = input()
#     M = list(map(int, input().split()))
#     lst = []  # 숫나사
#     lis = []  # 암나사
#     result = []
#     for n in range(0, int(N)):
#         lst.append(M[n * 2])
#         lis.append(M[n * 2 + 1])
#     for a in range(len(lis)):
#         if lst[a] not in lis:
#             result.append(lst[a])
#             result.append(lis[a])
#     for k in range(int(N)):
#         for m in range(int(N)):
#             if result[-1] == lst[m]:
#                 result.append(lst[m])
#                 result.append(lis[m])
#     res = list(map(str, result))
#     print('#{} {}'.format(i + 1, ' '.join(res)))
