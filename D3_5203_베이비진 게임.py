T = int(input())
for t in range(T):
    lst = list(map(int, input().split()))
    player1 = []
    player2 = []
    res = [0, 0]
    for i in range(12):
        if i % 2:
            player2.append(lst[i])
        else:
            player1.append(lst[i])
    player1.sort()
    player2.sort()
    # print(player1, player2)

    for p in player1:
        if player1.count(p) >= 3:
            res[0] += 1
        else:
            if p+1 in player1 and p+2 in player1:
                res[0] += 1

    for p in player2:
        if player2.count(p) >= 3:
            res[1] += 1
        else:
            if p+1 in player2 and p+2 in player2:
                res[1] += 1

    if res[0] < res[1]:
        res = 2
    elif res[0] > res[1]:
        res = 1
    else:
        res = 0

    print("#{} {}".format(t+1, res))

