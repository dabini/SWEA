T = int(input())
for t in range(T):
    N, K = map(int, input().split())
    score_lst = list(map(int, input().split()))
    ans = 0
    while K:
       ans += max(score_lst)
       score_lst.remove(max(score_lst))
       K -= 1
    print("#{} {}".format(t+1, ans))