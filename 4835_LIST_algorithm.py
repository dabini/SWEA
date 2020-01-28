#N개의 정수가 들어있는 배열에서 이웃한 M개의 합을 계산하는 것은 디지털 필터링의 기초연산이다.
#M개의 합이 가장 큰 경우와 가장 작은 경우의 차이를 출력하는 프로그램을 작성하시오.

T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    a = list(map(int, input().split()))

    lst = []
    for k in range(len(a)-M+1):
        total = 0
        for m in range(k, k+M):
            total += a[m]
        lst.append(total)

    max_num = max(lst)
    min_num = min(lst)
    print('#{0} {1}'.format(t+1, max_num-min_num))