# def find(n, k):
#     global score
#     if score not in scores:
#         scores.append(score)
#     for i in range(num):
#         if check[i] == 0:
#             check[i] = 1
#             score += num_lst[i]
#             find(n+1, k)
#             check[i] = 0
#             score -= num_lst[i]
# T = int(input())
#
# for t in range(T):
#     num = int(input())
#     num_lst = list(map(int, input().split()))
#     check = [0] * num
#     scores = set()
#     score = 0
#     find(0, num-1)
#     # print(scores)
#     print("#{} {}".format(t+1, len(scores)))

T = int(input())
for t in range(T):
    N = int(input())
    num_lst = list(map(int, input().split()))
    scores = set()
    scores.add(num_lst[0])
    for i in range(1, N):
        for j in list(scores):
            scores.add(num_lst[i] + j)
        scores.add(num_lst[i])
    print('#{} {}'.format(t+1, len(scores) + 1))