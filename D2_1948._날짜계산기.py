T = int(input())
days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for t in range(T):
    mon1, day1, mon2, day2 = map(int, input().split())
    res = 0
    if mon1 == mon2:
        res = day2 - day1 +1
    else:
        for i in range(mon1, mon2):
            res += days[i]
        res += day2 - day1 +1
    print('#{} {}'.format(t+1, res))