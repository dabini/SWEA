#크기가 N인 파스칼의 삼각형을 만들어야 한다.
#파스칼의 삼각형이란 아래와 같은 규칙을 따른다.
# ...
# 1. 첫 번째 줄은 항상 숫자 1이다.
#
# 2. 두 번째 줄부터 각 숫자들은 자신의 왼쪽과 오른쪽 위의 숫자의 합으로 구성된다

T = int(input())

for t in range(T):
    print('#{}'.format(t+1))
    num = int(input())
    pascal = [[0 for n in range(num)] for nu in range(num)]

    for i in range(num):
        pascal[i][0] = 1
        pascal[i][i] = 1

    for i in range(2, num):
        for j in range(1, i):
            pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]

    for i in range(num):
        for j in range(num):
            print(pascal[i][j], end=' ') if pascal[i][j] != 0 else print('', end='')
        print('')