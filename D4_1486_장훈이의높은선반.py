T = int(input())

for t in range(T):
    N, B = map(int, input().split()) #점원의 수 N, 선반의 높이 B
    h_lst = list(map(int, input().split()))
    ans = []
    for i in range(1 << len(h_lst)):
        tmp = []
        for j in range(len(h_lst)):
            if i & (1 << j):
                tmp.append(h_lst[j])
            if sum(tmp) >= B:
                ans.append(sum(tmp))
    res = min(ans) - B
    print("#{} {}".format(t+1, res))