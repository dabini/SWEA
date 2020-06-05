T = int(input())

for t in range(T):
    N, B = map(int, input().split()) #점원의 수 N, 선반의 높이 B
    h_lst = list(map(int, input().split()))
    ans = []