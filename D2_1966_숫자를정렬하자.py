# 주어진 N 길이의 숫자열을 오름차순으로 정렬하여 출력하라.
TC = int(input())

for tc in range(TC):
    N = int(input())
    test = list(map(int, input().split()))
    test.sort()
    test = list(map(str, test))
    k = ' '.join(test)
    print("#{} {}".format(tc+1, k))