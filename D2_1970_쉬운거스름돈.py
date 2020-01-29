T = int(input())
mon_lst = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
for t in range(T):
    money = int(input())
    lst = ['0'] * len(mon_lst)
    for i in range(len(mon_lst)):
        if money - mon_lst[i] >= 0:
            lst[i] = str(money // mon_lst[i])
            money -= mon_lst[i] * (money // mon_lst[i])
    print("#{}".format(t+1))
    print(' '.join(lst))