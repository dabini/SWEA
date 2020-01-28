#숫자 N은 아래와 같다.
#N=2a x 3b x 5c x 7d x 11e
#N이 주어질 때 a, b, c, d, e 를 출력하라.

T = int(input())
for t in range(T):
    N = int(input())
    cnt_lst = [0] *5
    n_lst = [2, 3, 5, 7, 11]

    while N > 1:
        for i in range(len(n_lst)):
            if N % n_lst[i] == 0:
                cnt_lst[i] += 1
                N //= n_lst[i]
    cnt = ' '.join(map(str, cnt_lst))
    print(f'#{t+1} {cnt}')

