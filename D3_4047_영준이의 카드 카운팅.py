T = int(input())

for t in range(T):
    check = True
    card_lst = []
    num_lst = [13, 13, 13, 13] #SDHC

    card = input()
    for i in range(0, len(card), 3):
        card_lst += [card[i] + card[i+1] + card[i+2]]

    for c in card_lst:
        if card_lst.count(c) > 1:
            check = False
        else:
            if c[0] == 'S':
                num_lst[0] -= 1
            elif c[0] == 'D':
                num_lst[1] -= 1
            elif c[0] == 'H':
                num_lst[2] -= 1
            elif c[0] == 'C':
                num_lst[3] -= 1


    if check is True:
        print("#{} {}".format(t+1, " ".join(list(map(str, num_lst)))))
    else:
        print("#{} ERROR".format(t + 1))
