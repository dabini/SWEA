T = int(input())

for t in range(T):
    price_lst = list(map(int, input().split()))
    cnt_lst = list(map(int, input().split()))

    for cnt in cnt_lst:
        if cnt != 0:
