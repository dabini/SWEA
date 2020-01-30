T = int(input())

for t in range(T):
    N, K = map(int, input().split())
    score = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    scores = []
    for n in range(N):
        mid, fin, hw = map(int, input().split())
        total = 0.35 * mid + 0.45 * fin + 0.2 * hw
        scores.append(total)
    lst = sorted(scores, reverse=True)

    new_score = []
    for j in range(len(score)):
        for k in range(N // 10):
            new_score.append(score[j])

    idx = lst.index(scores[K-1])
    print('#{} {}'.format(t+1, new_score[idx]))